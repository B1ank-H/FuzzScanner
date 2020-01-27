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

