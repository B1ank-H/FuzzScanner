# coding=utf-8
import os
import sys
import time
import queue
import random
import threading
import dns.resolver
#采用dns子域名爆破的方式，可自行更换指定字典
#注意：过大的字典会使电脑卡机
#由于dns和字典的原因，每次查询结果可能会不同

'''
通过多线程提高速度
支持参数输入，示例：python subdomain.py -f domain.csv -d qq.com -t 2 -o a.txt
若未指定输出文件，本程序会自动在本目录生成subdomain.txt存放子域名.
若未指定字典文件，本程序会自动搜寻本目录下的domain.csv.
若未指定超时时间，本程序自动设置一秒
其他内容请 python subdomain.py -h
'''

dnsservers = [
    '119.29.29.29', '182.254.116.116',
    '8.8.8.8', '8.8.4.4',
    '180.76.76.76',
    '1.2.4.8', '210.2.4.8',
    '101.226.4.6', '218.30.118.6',
    '8.26.56.26', '8.20.247.20'
]

class domainFuzzer(object):  # 爆破枚举

    def __init__(self,target,domainflie,outfile,time):
        self.target = target
        self.file = domainflie
        self.outfile = outfile
        self.time = int(time)

    def run(self):#创建使用队列
        input, output = queue.Queue(), queue.Queue()
        self.readFile(input,output)

    def dnssearch(self,sub,output,flag=0):  # 查询域名是否存在
        if flag:
            dns.resolver.Resolver().nameservers = [random.choice(dnsservers), random.choice(dnsservers)]#更改dns
        try:
            if dns.resolver.query(sub, 'A'):
                print(('Find: ')+(sub))
                output.put(sub)
                sys.stdout.flush()
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.Timeout :
            if not flag:
                self.dnssearch(sub,output,flag=1) # 更改dns再次尝试
            else:
                pass
        except Exception:
            pass

    def readFile(self,input,output):  # 使用队列拼接子域名头
        threads = []
        with open(self.file, "r") as csvfile:
            for line in csvfile.readlines():
                input.put('.'.join([str(line.strip()), str(self.target)]))
                while not input.empty():
                    sub = input.get_nowait()
                    t = threading.Thread(target=(self.dnssearch), args=(sub,output))
                    threads.append(t)
                    t.start()
        csvfile.close()
        for t in threads:
            t.join(self.time)
        self.writefile(output)

    def writefile(self,output):  # 文件写入
        while not output.empty():  # 判断队列是否不为空
            data = output.get()
            with open(self.outfile, "a") as file:
                    file.write((data)+ '\n')
            file.close()
        print(("\nResult has been written in ") + (self.outfile))
