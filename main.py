import xml.etree.ElementTree as ET

# read XMLdata
tree = ET.parse('yahoo-news-rss/news-202003042125.xml')
# get top elements
root = tree.getroot()

for child in root.iter():
    print(child.text)
