import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r = requests.get(link, headers= headers)

soup = BeautifulSoup(r.text,"html.parser")
print (soup.prettify())
