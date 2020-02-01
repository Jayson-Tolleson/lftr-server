#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# enable debugging
import cgitb
cgitb.enable()




print ("Content-Type: text/html")     # HTML is following
print                               # blank line, end of headers
print ('<html>')

print('''<head>








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


</body>
</div></div>
    <div id="content_footer"></div>''')

import feedparser

feed = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")

feed_title = feed['feed']['title']

feed_entries = feed.entries

for entry in feed.entries:
    article_title = entry.title
    article_link = entry.link
    print ("<marquee>" + article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title,article_title + "</marquee>")
    print (article_title)
