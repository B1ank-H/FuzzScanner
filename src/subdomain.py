# coding=utf-8
import os
import sys
import time
import queue
import random
import threading
import dns.resolver


dnsservers = [
    '119.29.29.29', '182.254.116.116', #腾讯DNS
    '223.5.5.5', '223.6.6.6', #阿里DNS
    '101.226.4.6'

]

class domainFuzzer(object):  # 爆破枚举

    def __init__(self,target,outfile,time):
        self.target = target
        self.file = 'domain.csv'
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
