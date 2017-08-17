from __future__ import print_function
import urllib2
from bs4 import BeautifulSoup
import pandas
import re


android_urls = ['https://www.analyticsvidhya.com/blog/2017/01/the-most-comprehensive-data-science-learning-plan-for-2017/']
   

def data_extract(url):
    
    #for name in urls:
    request = urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
    
    url_content = urllib2.urlopen(request).read()

    soup = BeautifulSoup(url_content, "html.parser")

    if soup.find('title') is not None:
        title = soup.find('title').text.strip()
    else:
        title = ''

    return("["+title+"]("+url+")")


f = open('C:/Users/SA31/Desktop/readme.txt')
fo = open('C:/Users/SA31/Desktop/readme_o.txt','w')
next = f.readline()
while next != "":
    print(next)
    next_url = re.findall('[^(]http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', next)
    next_url = ''.join(next_url)
    #print('once')
    if(len(next_url)>0):
        #print('once')
        #print(next_url)
        print(data_extract(next_url.strip()).encode('ascii', 'ignore'),file=fo)
    else:
        print(next,file=fo)
    next = f.readline()
    
 
fo.close()    
    
#data_extract(android_urls)
