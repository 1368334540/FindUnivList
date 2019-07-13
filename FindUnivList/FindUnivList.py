import requests
from bs4 import BeautifulSoup
# 定义总的大学数据列表
allUnivList=[]
def getHTMLText(url):
    try:
        #通过requests的get请求访问地址
        r=requests.get(url)
        #判断返回情况，如果非200，抛出异常，执行except
        r.raise_for_status()
        #修改html内容格式为utf-8
        r.encoding="utf-8"
        #返回响应后的网页内容
        return r.text
    except:
        return ""
    #填充大学排名二维列表的方法，解析和筛选html内容
def fillUnivList(soup):
    #通过BeautifulSoup对象调用findall方法，查找所有<tr>标签
    data=soup.find_all("tr")
    #遍历所有查到的<tr>标签
    for tr in data :
        #通过<tr>标签对象，调用findall方法，查找所有<td>标签
        ltd=tr.find_all("td")
        #剔除<td>为空的情况
        if len(ltd)==0:
            continue
            #创建一维列表，用于存放某一大学的所有信息
        singleUniv=[]
        #遍历某一大学<td>标签下的所有信息
        for td in ltd:
            #将<td>string拼接到单列表里
            singleUniv.append(td.string)
            #循环结束，完成一个大学的信息填充
        allUnivList.append(singleUniv)
    print(allUnivList)
    #打印二维数据的方法
def printUnivList(num):
    #列表头
    print("{0:{7:}^4}{1:{7:}^10}{2:{7:}^10}{3:{7:}^6}{4:{7:}^10}{5:{7:}^7}{6:{7:}^7}".format("排名","学校名称","省市","总分","生源质量","就业率","培养规模",chr(12288)))
    #二维数据遍历打印
    for i  in  range(num):
        u=allUnivList[i]
        print("{0:{7:}^4}{1:{7:}^10}{2:{7:}^10}{3:{7:}^10}{4:{7:}^10}{5:{7:}^10}{6:{7:}^10}".format(u[0],u[1],u[2],u[3],u[4],u[5],u[6],chr(12288)))


#定义主方法函数
def main():
    #爬出地址
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html"
    #通过requests库获取地址里的text
    text = getHTMLText(url)
    #用text获取BeautifulSoup对象
    soup=BeautifulSoup(text,"html.parser")
    #通过BeautifulSoup对象抓<tr>/<td>的string ，并放在二维数据中
    fillUnivList(soup)
    #打印二维数据，排名前100名的大学
    printUnivList(100)
#执行主函数
main()