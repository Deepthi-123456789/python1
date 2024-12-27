import requests
from bs4 import BeautifulSoup
url ="https://books.toscrape.com/"
r=requests.get(url)
#print(r.status_code) ###using only reusests
#print(r.text)      ###using only reusests
#print(r.text)
soup=BeautifulSoup(r.text,"html")
#print(soup)  ###gets full html code
print(soup.div)  ###only div tag data will be getting
print(soup.h3.string)