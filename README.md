# FuzzScanner
## Introduction
This is an integrated package.
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
## Example
#### Subdomain scan
```
FuzzScanner.py -sd -d qq.com -o result.txt
```
#### Open port scan
```
FuzzScanner.py -p -d www.qq.com
```
#### Alive detect
```
FuzzScanner.py -a -d 202.202.43.125
```
#### Waf detect 
```
FuzzScanner.py -w -d www.qq.com
```
#### Sql inject detect 
```
FuzzScanner.py -s -d http://111.198.29.45:43529/?inject=1
```
#### Information disclosure detect
```
FuzzScanner.py -i -d http://web.jarvisoj.com:32798/
```

