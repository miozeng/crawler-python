'''

@author: mio
'''
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup 
from download import request
import os

class Douban():
    
    # find movie title
    def all_movie(self,url):
        #html = self.request(url)
        html = request.get(url, 3)
        all_title =  BeautifulSoup(html.text, 'lxml')("span",{"class":"title"})
        for title in all_title: 
            print(title.get_text())

    # find movie img and save it
    def get_img(self,url): 
        self.mkdir()
        #html = self.request(url)
        html = request.get(url, 3)
        all_img =  BeautifulSoup(html.text, 'lxml').find('div', class_='article').find_all('img')
        for img in all_img: 
            img_url = img.get('src')
            print(img_url)
            self.save(img_url)

    def save(self, img_url):
        name = img_url[-12:-4]
        print(name)
        img = self.request(img_url)
        f = open("D:\\douban\\"+name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self):
        isExists = os.path.exists(os.path.join("D:\douban"))
        if not isExists:
            os.makedirs(os.path.join("D:\douban"))
            os.chdir(os.path.join("D:\douban"))
            return True
        else:
            return False

    def request(self, url): 
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content

douban = Douban()
douban.all_movie('http://movie.douban.com/top250?start=0&filter=') 
#douban.get_img('http://movie.douban.com/top250?start=0&filter=') 
#douban.all_movie('http://movie.douban.com/top250?start=25&filter=') 
#douban.get_img('http://movie.douban.com/top250?start=25&filter=')
  
        