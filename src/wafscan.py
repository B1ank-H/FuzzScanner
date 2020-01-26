# coding=utf-8
import re
import sys
import time
import requests
from poc import *  # waf指纹
from multiprocessing import Pool


class wafscan(object):

    def __init__(self,url):
        self.url = url
        self.dna = dna.strip().splitlines()
        self.name = ''
        self.normal_code = 0
        self.attack_code = 0

    def run(self):
        if '://' not in self.url:
            self.url = 'http://' + self.url
        if not self.url.endswith('/'):
            self.url = self.url + "/"
        if self.scan():
            print('[!]' + self.url + ' The waf name: ' + self.name)
            sys.stdout.flush()
        elif self.attack():
            print('The site ' + self.url + ' seems to be behind a WAF or some sort of security solution')
            print('Reason: The server returned a different response code when a string trigged the blacklist.')
            print('Normal response code is "' + str(self.normal_code) + '", while the response code to an attack is "' + str(self.attack_code) +'"')
        else:
            print('[x]' + self.url + ' Don\'t find the waf')
            sys.stdout.flush()



    def scan(self):
        try:
            r = requests.get(self.url)
            self.normal_code = r.status_code
            if r.status_code == 200:
                if self.identify(str(r.headers), str(r.content)):
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False

    def identify(self,header,page):
        for data in self.dna:
            name, location, value = data.strip().split("|", 2)
            self.name = name
            if location == "headers":
                if  re.search(value, header, re.I):
                    return True
            if location == "url":
                if re.search(value, page, re.I):
                    return True
        return False

    def attack(self):
        xsstring = '<script>alert("XSS");</script>'
        sqlistring = "UNION SELECT ALL FROM information_schema AND ' or SLEEP(5) or '"
        lfistring = '../../../../etc/passwd'
        rcestring = '/bin/cat /etc/passwd; ping 127.0.0.1; curl google.com'
        xxestring = '<!ENTITY xxe SYSTEM "file:///etc/shadow">]><pwn>&hack;</pwn>'
        results = []
        pool = Pool(processes=5)
        results.append(pool.apply_async(self.code_scan, (self.url + xsstring,)))
        results.append(pool.apply_async(self.code_scan, (self.url + sqlistring,)))
        results.append(pool.apply_async(self.code_scan, (self.url + lfistring,)))
        results.append(pool.apply_async(self.code_scan, (self.url + rcestring,)))
        results.append(pool.apply_async(self.code_scan, (self.url + xxestring,)))
        pool.close()
        pool.join()
        for r in results:
            if self.normal_code != r.get():
                self.attack_code = r.get()
                return True
        return False

    def code_scan(self,string):
        return requests.get(string).status_code