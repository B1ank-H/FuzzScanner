# coding=utf-8
import sys
import queue
import requests
import threading
from src.colour import Red,Green
from multiprocessing import Pool,Manager


header = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
dict_name = ['svn', 'git']
dict_target = {'svn': '.svn/entries', 'git': '.git/config'}

class IDFuzzer(object):

	def __init__(self,domain):
		self.domain = domain
		self.UA = {'User-Agent': header}

	def run(self):#判断是否有http://，设置进程池
		self.check()
		flag = Manager().Value('H', 1)
		pool = Pool(processes=16)
		input = queue.Queue()
		with open('php-name.csv', "r") as csv0:
			for line0 in csv0.readlines():
				with open('backup-name.csv', "r") as csv1:
					for line1 in csv1.readlines():
						input.put('.php'.join([str(line0.strip()), str(line1.strip())]))
		for name in dict_name:
			pool.apply_async(self.scan, args=(name, self.domain + dict_target[name],flag))
		while not input.empty():
			sub = input.get_nowait()
			pool.apply_async(self.scan, args=(None, self.domain + sub,flag))
		csv0.close()
		csv1.close()
		pool.close()
		pool.join()
		if flag.value:
			Red('[x]Don\'t find anything\n')

	def check(self):
		if '://' not in self.domain:
			self.domain = 'http://' + self.domain
		if not self.domain.endswith('/'):
			self.domain = self.domain + "/"

	def judge(self,name,request):#查询特征值
		if name == 'svn':
			if 'dir' in str(request.content, encoding = "utf-8") and 'svn' in str(request.content, encoding = "utf-8"):
				return True
			else:
				return False
		elif name == 'git':
			if 'repositoryformatversion' in str(request.content, encoding = "utf-8"):
				return True
			else:
				return False
		else:
			return True

	def scan(self,name,target,flag): # 探测git/svn文件泄漏
		try:
			r = requests.head(url=target,headers=self.UA,timeout=5)
			if r.status_code == 200:
				request = requests.get(url=target, headers=self.UA, timeout=5)
				if self.judge(name,request):
					Green ('[!]' + target + '\n')
					flag.value = 0
				else:
					pass
			else:
				pass
		except:
			pass