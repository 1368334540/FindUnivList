from urllib import request
url=r"http://www.baidu.com"
response= request.urlopen(url).read().decode()
print(response)