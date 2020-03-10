import xml.etree.ElementTree as ET

# read XMLdata
tree = ET.parse('yahoo-news-rss/news-202003042125.xml')
# get top elements
root = tree.getroot()

path = 'text/outpu.txt'
with open(path,mode='a') as f:
    for child in root.iter(tag='title'):
        f.write(child.text+"\n")
f.close()
