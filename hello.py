import  requests
r = requests.get("http://www.baidu.com");
print(r.status_code)
print(r.text)
print(r.encoding)
r.encoding="utf-8";
print(r.encoding)
print(r.text)