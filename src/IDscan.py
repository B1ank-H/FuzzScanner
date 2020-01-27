# coding=utf-8
import sys
import queue
import requests
import threading
from multiprocessing import Pool
from src.colour import Red,Green

header = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
dict_name = ['svn', 'git']
dict_target = {'svn': '.svn/entries', 'git': '.git/config'}

class IDFuzzer(object):

	def __init__(self,domain):
		self.domain = domain
		self.UA = {'User-Agent': header}

	def run(self):#判断是否有http://，设置进程池
		self.check()
		pool = Pool(processes=3)
		for name in dict_name:
			pool.apply_async(self.scan, args=(name,self.domain+dict_target[name]))
		pool.apply_async(self.file_bak, args=())
		pool.close()
		pool.join()

	def check(self):
		if '://' not in self.domain:
			self.domain = 'http://' + self.domain
		if not self.domain.endswith('/'):
			self.domain = self.domain + "/"

	def judge(self,name,request):#查询特征值
		if name == 'svn':
			if 'dir' in str(request.content, encoding = "utf-8") and 'svn' in str(request.content, encoding = "utf-8"): return True
			else: return False
		elif name == 'git':
			if 'repositoryformatversion' in str(request.content, encoding = "utf-8"): return True
			else: return False
		else: return True

	def scan(self,name,target): # 探测git/svn文件泄漏
		try:
			r = requests.head(url=target,headers=self.UA,timeout=5)
			if r.status_code == 200:
				try:
					request = requests.get(url=target, headers=self.UA, timeout=5)
					if self.judge(name,request):
						Green('[!]' + target + '\n')
					else:
						pass
				except:
					pass
			else:
				pass
		except:
			pass

	def file_bak(self): #探测备份文件泄漏
		input = queue.Queue()
		threads = []
		with open('php-name.csv', "r") as csv0:
			for line0 in csv0.readlines():
				with open('backup-name.csv', "r") as csv1:
					for line1 in csv1.readlines():
						input.put('.php'.join([str(line0.strip()), str(line1.strip())]))
		while not input.empty():
			sub = input.get_nowait()
			t = threading.Thread(target=(self.scan_base), args=(sub, self.domain+sub))
			threads.append(t)
			t.start()
		for t in threads:
			t.join(1)
		csv1.close()
		csv0.close()