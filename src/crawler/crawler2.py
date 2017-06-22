# -*- coding: utf-8 -*-
'''
Created on 2017621

@author: mio
'''
import urllib2
import urllib

#head
url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 

#反盗链
#headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
#                       'Referer':'http://www.zhihu.com/articles' }  

#proxy
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#PUT or DELETE 
#request = urllib2.Request(uri, data=data)
#request.get_method = lambda: 'PUT' # or 'DELETE'
#response = urllib2.urlopen(request)

#DebugLog
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

#Error
req = urllib2.Request('http://sss.com.r')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"