#!/usr/bin/env python
import requests
import optparse
import sys
def parser():
    par = optparse.OptionParser()
    par.add_option("-u", "--url", dest='url', help="use -u for add url")
    (options, argument) = par.parse_args()
    if not options.url:
        print("[-]Please enter a url or use '-h' or '--h' for info")
        sys.exit()
    return options
def payload(url):
    with open("file/xss.txt", 'r+') as file:
        lists = file.readlines()
        for payloads in lists:
            Furl = str(url)+str(payloads)
            res = requests.get(Furl)
            if res:
                print("Got url------>" + Furl)
        print("[+]Attack Failed")
if __name__ == "__main__":
    print("[+]Attack Started[+]")
    options = parser()
    payload(options.url)
