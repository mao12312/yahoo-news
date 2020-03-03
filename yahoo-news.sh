#!/bin/bash
date=$(date +'%Y%m%d%H%M')
dirname="/Users/ohmuramao/bot/yahoo-new-rss"
mkdir -p $dirname
filename="$dirname/news-$date.xml"
echo "save to $filename"
curl -s -o $filename -H "User-Agent: CrawlBot; awsedrft039@gmail.com" https://news.yahoo.co.jp/pickup/economy/rss.xml
