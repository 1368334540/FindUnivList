import requests
from bs4 import BeautifulSoup
import re
r=requests.get("http://www.baidu.com")
r.encoding="utf-8"
soup=BeautifulSoup(r.text)
a=soup.find_all('a',{'href':re.compile("news")})
print(a)
print(len(a))

