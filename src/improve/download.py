'''

@author: admin
'''
# -*- coding: utf-8 -*-
import requests
import random
import time

class download:
    
    def __init__(self):
        # get proxy ip
        self.iplist = ["211.155.234.99","218.75.100.114","125.39.129.67"]  
       
        # get head
        self.user_agent_list = [
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
             "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
             "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
             "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
             "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
         ]
 
    def get(self, url, timeout, proxy=None, num_retries=6): 
        print(u'start：', url)
        UA = random.choice(self.user_agent_list) ## get a random String from self.user_agent_list
        headers = {'User-Agent': UA}  
 
        if proxy == None: ##
            try:
                return requests.get(url, headers=headers, timeout=timeout)
            except:#if exception 
 
                if num_retries > 0: ##num_retries is Repeat times
                    time.sleep(10) ##delay 10s
                    print('repeat：', num_retries)
                    return self.get(url, timeout, num_retries-1)  ##
                else:
                    print('use proxy')
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip()) 
                    proxy = {'http': IP}
                    return self.get(url, timeout, proxy,) 
 
        else: 
            try:
                IP = ''.join(str(random.choice(self.iplist)).strip()) ##get random ip from elf.iplist
                proxy = {'http': IP} 
                return requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
            except:
 
                if num_retries > 0:
#                     time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    print('repeat：', num_retries)
                    print('proxy is', proxy)
                    return self.get(url, timeout, proxy, num_retries - 1)
                else:
                    print('oh no i can\'t do it' )
                    return self.get(url, 3)

        
request = download()