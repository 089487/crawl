#coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import pdfkit
import pdfcrowd
import sys

function={"http://www.cpbl.com.tw/":{"news":'^/news/view/'}}
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
class Crawler():
    def html_to_pdf(self,html,filename):
        try:
            print(filename)
    # create the API client instance
            filename+='.pdf'
            client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
            client.setPageSize(u'A2')
            client.setHeaderHeight(u'0.0in')
            client.setNoMargins(True)
            # run the conversion and write the result to a file
            client.convertFileToFile(html,filename)
        except pdfcrowd.Error as why:
            # report the error
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
            raise
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
    def news(self,url,filename):
        #os.system("cls")
        #print(url)
        html=urlopen(url)
        page=html.read()
        bs=BeautifulSoup(page,'html.parser')
        title=bs.find('div',{'class':'news_title'})
        time=title.find('span').string
        #print(page)
        f=open('new.html',"wb")
        f.write(page)
        f.close()
        fail=self.html_to_pdf('new.html',time+filename)
        if fail==True:
            return
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
                filename=tag.string.replace(' ','').replace(':','比')
                self.news(str(url+tag['href']),filename)
                #print(tag.string,':',)
crawler=Crawler()
crawler.parse("http://www.cpbl.com.tw/","news")
#print(bs.prettify())
