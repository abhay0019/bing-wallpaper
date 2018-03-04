#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import os
import datetime 

proxies = {
  'http': 'http://edcguest:edcguest@172.31.102.29:3128/',
  'https': 'https://edcguest:edcguest@172.31.102.29:3128/'
}
dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
if not os.path.isdir('/home/abhay/Desktop/Bing'):
  os.mkdir('/home/abhay/Desktop/Bing')
url = 'http://bingwallpaper.com/UK' 
#sc = requests.get(url,proxies=proxies)
sc = requests.get(url)
soup = BeautifulSoup(sc.text)
urls=soup.find_all('img')
#image_ret=requests.get(urls[1].get('src'),proxies=proxies)
image_ret=requests.get(urls[1].get('src'))
direct=os.path.join('/home/abhay/Desktop/Bing',cd+'.jpg')  
with open(direct,'wb') as f:
  f.write(image_ret.content)
  f.close()
  
os.system('gsettings set org.gnome.desktop.background picture-uri file:///home/abhay/Desktop/Bing/'+cd+'.jpg')
