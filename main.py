from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import sys
import os
function={"http://www.cpbl.com.tw/":{"news":'^/news/view/'}}
class Crawler():
    def __init__(self):
        self.session=requests.session()
        self.headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36',
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
        page=self.setforchinise(html.read().decode('utf-8'))
        #print(page)
        
        bs=BeautifulSoup(page,'html.parser')
        l=bs.find_all('p')
        for text in l:
            print(text.string)
    def parse(self,url,chose):
        print(url)
        html=urlopen(url)
        page=self.setforchinise(html.read().decode('utf-8'))
        print(page)
        limit=function[url][chose]
        self.bs=BeautifulSoup(page,'html.parser')
        l=self.findhref('a',limit)
        if chose=="news":
            for tag in l:
                self.news(str(url+tag['href']))
                print(tag.string,':',)
crawler=Crawler()
crawler.parse("http://www.cpbl.com.tw/","news")
#print(bs.prettify())
