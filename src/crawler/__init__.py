# -*- coding: utf-8 -*-
import urllib2
import urllib

#urlopen(url, data, timeout) 
#第一个参数url即为URL(非空)，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
#如果第二个参数data为空那么要特别指定是timeout是多少，写明形参，如果data已经传入，则不必声明。
#    response = urllib2.urlopen('http://www.baidu.com', timeout=10)
#    response = urllib2.urlopen('http://www.baidu.com',data, 10)
    
#simple demo
response = urllib2.urlopen("http://www.baidu.com")
print response.read()
print("end")


#Request
request = urllib2.Request("http://www.baidu.com")
response2 = urllib2.urlopen(request)
print response2.read()

#POST
values = {"username":"mio","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://localhost:8080/account/login2"
requestPost = urllib2.Request(url,data)
responsePost = urllib2.urlopen(requestPost)
print responsePost.read()

#GET
valuesGet={}
valuesGet['username'] = "mio"
valuesGet['password']="XXXX"
dataGet = urllib.urlencode(valuesGet) 
urlGet = "http://localhost:8080/account/login"
geturl = urlGet + "?"+dataGet
requestGet = urllib2.Request(geturl)
responseGet = urllib2.urlopen(requestGet)
print responseGet.read()