# -*- coding: utf-8 -*-
'''
Created on 2017-6-21

@author: admin
'''
import urllib
import urllib2
import cookielib

#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

#创建MozillaCookieJar实例对象
cookiel = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookiel.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
reql = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
openerl = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiel))
responsel = openerl.open(reql)
print responsel.read()

#save cookie
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie1 = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler1 = urllib2.HTTPCookieProcessor(cookie1)
opener1 = urllib2.build_opener(handler1)
response1 = opener1.open("http://www.baidu.com")
#保存cookie到文件
cookie1.save(ignore_discard=True, ignore_expires=True)

#模拟cookie登录
#创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址
filename2 = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie2 = cookielib.MozillaCookieJar(filename2)
opener2 = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie2))
postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'23342321'
        })
#登录教务系统的URL
loginUrl2 = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result2 = opener2.open(loginUrl2,postdata)
#保存cookie到cookie.txt中
cookie2.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result2 = opener2.open(gradeUrl)
print result2.read()