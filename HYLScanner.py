import argparse
from src.wafscan import wafscan
from src.alivescan import alivescan
from src.IDscan import IDFuzzer
from src.portscan import portscan
from src.SQLiscan import sqlmap
from src.subdomain import domainFuzzer


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    parser.add_argument("-d", "--domain", metavar="", help="domain name")
    parser.add_argument("-f", "--file", metavar="", default="domain.csv", help="subdomains dict file name")
    parser.add_argument("-o", "--out", metavar="", default="subdomain.txt", help="result out file")
    parser.add_argument("-t", "--time", metavar="", default=1, help="timeout")