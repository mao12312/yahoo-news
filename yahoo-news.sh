#!/bin/bash
# date=$(date +'%Y%m%d%H%M')
dirname="/home/vagrant/workspace/yahoo-news/yahoo-news-rss"
mkdir -p $dirname
filename="$dirname/yahoo-rss.xml"
echo "save to $filename"
curl -s -o $filename -H "User-Agent: CrawlBot; awsedrft039@gmail.com" https://news.yahoo.co.jp/pickup/economy/rss.xml