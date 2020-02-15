# FuzzScanner

##  介绍
[![PyPI version](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/)  [![License](https://img.shields.io/badge/license-GPLv2-red.svg)](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/LICENSE) 

如果发现任何程序错误，可以向我发送电子邮件 MTM5ODk4MDUxNkBxcS5jb20=  。

## 功能

- 子域扫描
- 开放端口扫描
- 存活检测
- Waf检测
- SQL注入检测
- 信息泄露检测

## 用法

使用`FuzzScanner.py -h`查看帮助

```
用法：FuzzScanner.py [-h] [-d] [-a] [-s] [-p] [-w] [-sd] [-i] [-t] [-o]

可选参数：
  -h, --help        show this help message and exit
  -d , --domain     Select the domain or ip
  -a, --alive       Alive detection
  -s, --sql         Sql inject detection
  -p, --port        Open port detection
  -w, --waf         Waf name detection
  -sd, --subdomain  subdomain fuzz detection
  -i, --id          Information disclosure detection
  -t , --time       subdomains timeout setting
  -o , --out        subdomains result file
```

## 详细信息

#### 子域扫描

```
FuzzScanner.py -sd -d qq.com -o result.txt
```

如果未指定输出文件，则程序将在此目录中自动生成subdomain.txt以存储子域名。

如果未指定字典文件，则该程序将在此目录中自动搜索domain.csv。

注意：当心过大字典导致卡机

如果未指定超时，程序将自动设置一秒钟

#### 端口扫描

```
FuzzScanner.py -p -d www.qq.com
```

#### 存活检测

```
FuzzScanner.py -a -d 202.202.43.125
```

支持ICMP / SYN / ACK扫描

#### Waf检测

```
FuzzScanner.py -w -d www.qq.com
```

poc.py是waf指纹库

将普通URL状态代码与恶意请求状态代码进行比较，以检测其waf是否进行反扫描

#### SQL注入检测

```
FuzzScanner.py -s -d http://43.247.91.228:84/Less-1/?id=1
```

注意：**请自行找到注入点或使用awvs扫描注入点**

#### 信息泄露检测

```
FuzzScanner.py -i -d http://web.jarvisoj.com:32798/
```

支持检测git / svn，bak，swp和其他备份文件泄漏

如果php文件名不在php-name.csv中，请手动将找到的php文件名添加到php-name.csv中