import os
import argparse
from src.IDscan import IDFuzzer
from src.wafscan import wafscan
from src.SQLiscan import sqlmap
from src.portscan import portscan
from src.alivescan import alivescan
from src.subdomain import domainFuzzer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Select the domain or ip")
    parser.add_argument("-a", "--alive",action='store_true', help="Alive detection")
    parser.add_argument("-w", "--waf",action='store_true', help="Waf name detection")
    parser.add_argument("-t", "--time", default=1, help="subdomains timeout setting")
    parser.add_argument("-s", "--sql",action='store_true', help="Sql inject detection")
    parser.add_argument("-p", "--port", action='store_true',help="Open port detection")
    parser.add_argument("-o", "--out", default="subdomain.txt", help="subdomains result file")
    parser.add_argument("-sd", "--subdomain",action='store_true', help="subdomain fuzz detection")
    parser.add_argument("-i", "--id", action='store_true',help="Information disclosure detection")
    args = parser.parse_args()
    if not args.domain:
        exit('You don\'t have input the domain or ip')
    else:
        if args.subdomain:
            sub = domainFuzzer(args.domain,args.out,args.time)
            sub.run()
        if args.alive:
            alive = alivescan(args.domain)
            alive.run()
        if args.port:
            port = portscan(args.domain)
            port.run()
        if args.waf:
            waf = wafscan(args.domain)
            waf.run()
        if args.id:
            id = IDFuzzer(args.domain)
            id.run()
        if args.sql:
            sql = sqlmap(args.domain)
            sql.run()
