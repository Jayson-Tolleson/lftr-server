 #!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging


import cgitb
cgitb.enable()

from os import listdir
import cgi
import os
import subprocess
import time
from time import sleep
from bs4 import BeautifulSoup as bs
import requests
import re




print ('''Content-Type: text/html''') # HTML is following print 
print



#html to get 'searchterms'  from 'searchterms1' 
#create an form element from html input into python3

print ('''<html><head>













  <title>J^2</title>
  <meta name="description" content="=100jay" />
  <meta name="keywords" content="Music, Art, Forum" />
  <meta http-equiv="content-type" content="text/html" />
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style>
body {background: #1339de;}
</style>
<body>
  <div id="main">
    <div id="site_content">
      <div id="content">

<h1>archive.org movie maker</h1>
<h1>otw in python-html</h1>
<h1>when available submit and run script for 15 min to see made video populate</h1>
<script></script>
<form>
input search terms 1: <input type = "name" name = "searchterms1" value = "fly+fishing">  <br />
<input type = "submit" value = "Submit" />
Try It</button>
</form>
''')





#python3 programming
#create a form element from html input
form = cgi.FieldStorage()

#get value of html input and make it a python variable
searchterms = form.getvalue("searchterms1","freediving")
#print python variables
print (form)
print (searchterms)
#html video element ....visable upon final loading
print ('download @ https://lftr.biz/movies/yoursearchterms.mp4')

print ('''<video src='https://lftr.biz/movie/'''+ searchterms) 
print ('''.mp4'></video></div></div></body></html>''')



#python scraper for movies on archive.org
print
site = ('https://archive.org/download')
url = ('https://archive.org/details/movies?and%5B%5D='+searchterms+'&sin=')
print ('URL:',url)
move = ('sudo rm -r /var/www/vids && sudo mkdir /var/www/vids && cd /var/www/vids')
del1 = ('sudo rm -r /var/www/vidsint && sudo mkdir /var/www/vidsint')
print (del1)
print (move)
subprocess.call(del1, shell=True, stderr=subprocess.STDOUT)
subprocess.call(move, shell=True, stderr=subprocess.STDOUT)
x = 1
r = requests.get(url)
webpage = r.text
soup = bs(webpage, 'html.parser')
for s in searchterms:
    sea=s
print (s)
links = [link.get('href') for link in soup.find_all('a', title=re.compile(sea), href=re.compile('details'))]

print (links)
videos = []
videos2 = []
for link in links:
    print (link)
    link=link[9:]
    videos.append(link)
print (videos)
for video in videos:
    print ('https://archive.org/download/'+video)
    r2 = requests.get('https://archive.org/download/'+video)
    webpage2 = r2.text
    soup2 = bs(webpage2, 'html.parser')
    links2 = [link2.get('href') for link2 in soup2.find_all('a', href=re.compile('.mp4'))]
    print (links2)
#    links2 = [link2.get('href') for link2 in soup2.find_all('a', attrs={'class':re.compile('')})]
    for link2 in links2:
        print (link2)
        wget=('cd /var/www/vids && sudo wget https://archive.org/download/%s/%s -O %d.mp4')%(video,link2,x)
        subprocess.call(wget, shell=True, stderr=subprocess.STDOUT)
        ff2 = ('sudo ffmpeg -ss 0:07 -i /var/www/vids/%s.mp4 -t 17.0 -vf scale=1280:720 -y /var/www/vidsint/%s-0.mp4') % (x,x)
        subprocess.call(ff2, shell=True, stderr=subprocess.STDOUT)
        ff21 = ('sudo ffmpeg -ss 0:30 -i /var/www/vids/%s.mp4 -t 0:30 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" -y /var/www/vids/%s-1.mp4 && sudo ffmpeg -i /var/www/vids/%s-1.mp4 -vf scale=1280:720 -y /var/www/vidsint/%s-1.mp4') % (x,x,x,x)
        subprocess.call(ff21, shell=True, stderr=subprocess.STDOUT)
        ff22 = ('sudo ffmpeg -ss 1:30 -i /var/www/vids/%s.mp4 -t 0:30 -vf scale=1280:720 -y /var/www/vidsint/%s-2.mp4') % (x,x)
        subprocess.call(ff22, shell=True, stderr=subprocess.STDOUT)
        ff23 = ('sudo ffmpeg -ss 2:20 -i /var/www/vids/%s.mp4 -t :20.0 -vf scale=1280:720 -y /var/www/vidsint/%s-3.mp4') % (x,x)
        subprocess.call(ff23, shell=True, stderr=subprocess.STDOUT)
        ff24 = ('sudo ffmpeg -ss 1:07 -i /var/www/vids/%s.mp4 -t 10.0 -vf scale=1280:720 -y /var/www/vidsint/%s-4.mp4') % (x,x)
        subprocess.call(ff24, shell=True, stderr=subprocess.STDOUT)
        ff25 = ('sudo ffmpeg -ss 2:07 -i /var/www/vids/%s.mp4 -t 10.0 -vf scale=1280:720 -y /var/www/vidsint/%s-5.mp4') % (x,x)
        subprocess.call(ff25, shell=True, stderr=subprocess.STDOUT)
        ff26 = ('sudo ffmpeg -ss 2:30 -i /var/www/vids/%s.mp4 -t 0:30 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" -y /var/www/vids/%s-6.mp4 && sudo ffmpeg -i /var/www/vids/%s-6.mp4 -vf scale=1280:720 -y /var/www/vidsint/%s-6.mp4') % (x,x,x,x)
        subprocess.call(ff26, shell=True, stderr=subprocess.STDOUT)
        print (x)
        x += 1
        print (x)
videoslist=[]
print

#combine video
f= open("/var/www/vidsint/vidslist.txt","w+")
list=os.listdir('/var/www/vidsint/')
print (list)
for l in list:
    if 11<len(l)< 13:
        f.write("\r\n")
    else:
        f.write("file '%s'\r\n" % l)
f.close()
ff10 = ('cd /var/www/vidsint/ && sudo ffmpeg -f concat -i /var/www/vidsint/vidslist.txt -c copy -y /var/www/movie/'+searchterms+'.mp4')
print (ff10)
subprocess.call(ff10, shell=True, stderr=subprocess.STDOUT)





print ('''<video src='https://lftr.biz/movie/'''+ searchterms) 
print ('''.mp4'></video></div></div></body></html>''')

