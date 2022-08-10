import requests
from lxml import etree

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r = requests.get(link, headers= headers)

html = etree.HTML(r.text)
title_list = html.xpath('//h1[@class="post-title"]/a/text()')
print (title_list)