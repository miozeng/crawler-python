# -*- coding: utf-8 -*-
'''
Created on 20176

@author: admin
'''
import urllib
import urllib2
import re

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request("https://www.qiushibaike.com/hot/",headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?content">(.*?)<!--(.*?)-->.*?</div>(.*?)'+
                         '<div class="stats.*?class="number">(.*?)</i>',re.S)
    pattern2 = re.compile('<div.*?content">(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    items2 = re.findall(pattern2,content)
    for item in items:
        print item[0],item[1],item[2],item[4]
        haveImg = request.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
    for item in items2:
        print item[0]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
        
#1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。
#2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。
#3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。