# FuzzScanner
## Introduction
This is an integrated package.

 If it has any program error,you can send email: MTM5ODk4MDUxNkBxcS5jb20=  to me. 

## Function
- Subdomain scan
- Open port scan
- Alive detect
- Waf detect 
- Sql inject detect
- Information disclosure detect
## Usage
use `FuzzScanner.py -h` to see help
```
usage: FuzzScanner.py [-h] [-d] [-a] [-s] [-p] [-w] [-sd] [-i] [-t] [-o]

optional arguments:
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
## Details&Nodes
#### Subdomain scan
```
FuzzScanner.py -sd -d qq.com -o result.txt
```
If no output file is specified, the program will automatically generate subdomain.txt in this directory to store the subdomain name.

If no dictionary file is specified, this program will automatically search for domain.csv in this directory.

Note: Beware of excessive card dictionary

If no timeout is specified, the program automatically sets one second


#### Open port scan
```
FuzzScanner.py -p -d www.qq.com
```
#### Alive detect
```
FuzzScanner.py -a -d 202.202.43.125
```
Support ICMP / SYN / ACK scanning
#### Waf detect 
```
FuzzScanner.py -w -d www.qq.com
```
poc.py is the waf fingerprint library

Comparing ordinary URL status codes with malicious request status codes to detect if their waf is anti-scanning
#### Sql inject detect 
```
FuzzScanner.py -s -d http://111.198.29.45:43529/?inject=1
```
Note: 
**Please find the injection point by yourself or scan the injection point with awvs**

#### Information disclosure detect
```
FuzzScanner.py -i -d http://web.jarvisoj.com:32798/
```
Support detection of git / svn, bak, swp and other backup file leaks

If the php file name is not in php-name.csv, please manually add the php file name you found to php-name.csv

