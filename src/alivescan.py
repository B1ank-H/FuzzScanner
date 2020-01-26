# coding=utf-8
import sys
import threading
from scapy.all import *
from multiprocessing import Pool

'''
支持icmp/svn/ack探测
支持参数输入，示例：python alivescan.py -d www.qq.com 
'''

class alivescan(object):

    def __init__(self,ip):
        self.url = ip
        self.flag = True


    def run(self):
        results = []
        pool = Pool(processes=3)
        results.append(pool.apply_async(self.icmp, ()))
        results.append(pool.apply_async(self.syn, ()))
        results.append(pool.apply_async(self.ack, ()))
        pool.close()
        pool.join()
        for res in results:
            if res.get() == 'YES':
                self.flag = False
                print(self.url + ' online')
                sys.stdout.flush()
                break
        if self.flag:
            print(self.url + ' offline')
            sys.stdout.flush()


    def icmp(self):
        try:
            result = sr1(IP(dst = self.url)/ICMP(),timeout = 3,verbose = False)
            if result:
                return 'YES'
            else:
                return 'NO'
        except:
           return 'NO'

    def syn(self):
        try:
            result = sr(IP(dst=self.url) / TCP(dport=443, flags=2), timeout=1, verbose=False)
            if result:
                return 'YES'
            else:
                return 'NO'
        except:
            return 'NO'

    def ack(self):
        try:
            result = sr(IP(dst=self.url) / TCP(dport=80, flags=1), timeout=1, verbose=False)
            if result:
                return 'YES'
            else:
                return 'NO'
        except:
            return 'NO'