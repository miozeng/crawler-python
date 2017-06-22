'''

@author: mio
'''
import urllib
import urllib2
import re

class Spider:

    def __init__(self):
        self.siteURL = 'http://www.baidu.com/s'
#User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
    def getPage(self,searchc):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent } 

        valuesGet={}
        valuesGet['wd']=searchc
        dataGet = urllib.urlencode(valuesGet) 
        url = self.siteURL + "?" + dataGet
        print url
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def getContents(self,searchc):
        page = self.getPage(searchc)
        print page
        pattern = re.compile('<div class="result c-container ".*?<h3.*?<a href="(.*?)".*?>(.*?)</a>',re.S)
        items = re.findall(pattern,page)
        #,item[1],item[2],item[3],item[4]
        for item in items:
            print item[1]

spider = Spider()
spider.getContents("python")