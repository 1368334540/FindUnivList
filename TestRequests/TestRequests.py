import  requests
def getHTMLTest(url):
    try:
        r= requests.get(url);
        r.raise_for_status();
        r.encoding="utf-8";
        return  r.text;
    except:
        return "";
text=getHTMLTest("http://www.baidu.com")
print(text)

