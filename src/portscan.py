# coding=utf-8
import os
import csv
import sys
import time
import queue
import threading
import linecache
from socket import *
from src.colour import Red,Green

class portscan(object):

    def __init__(self,domain_name):
        self.domain = domain_name
        self.port = queue.Queue()

    def scan(self, port):# 创建一个socket:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((self.domain, port))
        if result == 0:
            self.port.put(port)
        sock.close()

    def search_cell(self):
        while  not self.port.empty():
            data = self.port.get_nowait()
            with open('service-port.csv', 'r') as file: #读取数据对应csv的行号
                reader = csv.reader(file)
                for i, b in enumerate(reader):
                    if str(data) in b:
                        dates = linecache.getline('service-port.csv', i + 1) #读取csv指定行内容
                        port, name, service = dates.strip().split(",", 2)
                        print('{:5s}{:^18s}'.format(port, service))
                        #print (port + '      ' + '%15s' % service)
                        break
        file.close()

    def run(self):
        for port in range(0, 15000):
            t = threading.Thread(target=self.scan, args=(port,))
            t.start()
        self.search_cell()