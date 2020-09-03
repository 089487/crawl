from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import lxml
function={"http://www.cpbl.com.tw/":{"news":'^/news/view/'}}
class Crawler():
    def __init__(self):
        self.session=requests.session()
        self.headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X)'
                'AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobilr/11D257',
                'Accept': 'text/html,application/xhtml+xml,application/xml;'
                'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
                }
    def setforchinise(self,web):
        type=sys.getfilesystemencoding()
        web.encode(type)
        return web
    def findhref(self,tag,limit):
        return self.bs.find_all(tag,{'href':re.compile(limit)})
    def news(self,url):
        #os.system("cls")
        #print(url)
        html=urlopen(url)
        page=str(html.read())#self.setforchinise(html.read().decode('utf-8'))
        #print(page)
        f=open('new.html',"w")
        bs=BeautifulSoup(page,'html.parser')
        f.write(bs.text)
        f.close()
        os.system("pause")
    def parse(self,url,chose):
        #print(url)
        html=urlopen(url)
        page=self.setforchinise(html.read().decode('utf-8'))
        #print(page)
        limit=function[url][chose]
        self.bs=BeautifulSoup(page,'html.parser')
        l=self.findhref('a',limit)
        if chose=="news":
            for tag in l:
                self.news(str(url+tag['href']))
                #print(tag.string,':',)
crawler=Crawler()
crawler.parse("http://www.cpbl.com.tw/","news")
#print(bs.prettify())
