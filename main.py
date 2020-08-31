from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import requests
import re
class Crawler():
    def __init__(self):
        self.session=requests.session()
        self.headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;'
                'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
                }
    
    def findhref(self,tag,limit):
        return self.bs.find_all(tag,{'href':re.compile(limit)})
    def parse(self,url):
        print(url)
        html=urlopen(url)
        page=html.read()
        print(page)
        self.bs=BeautifulSoup(page,'html.parser')
        div=self.findhref('a','^/news/view/')
        print("div",div)
        for tag in div:
            print(tag.string,':',str(url+tag['href']))
crawler=Crawler()
crawler.parse("http://www.cpbl.com.tw/")
#print(bs.prettify())
