import requests
from bs4 import BeautifulSoup
url="https://tradenpl.com/"
req=requests.get(url)
Content= req.content
# print(Content)
soup=BeautifulSoup(Content,"html.parser")
# print(soup.prettify)
para=soup.find_all("h3")
print(para)