import xml.etree.ElementTree as ET

# read XMLdata
tree = ET.parse('yahoo-news-rss/yahoo-rss.xml')
root = tree.getroot()

path = 'output/outpu.txt'

with open(path, mode='a') as f:
    for child in tree.findall('.//item'):
        f.write(child.find('title').text+'\n')
        f.write(child.find('link').text+'\n')
f.close()