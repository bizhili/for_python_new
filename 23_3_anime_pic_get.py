import requests
from bs4 import BeautifulSoup
import re
import time


def main():
    time1=time.time()
    count=0
    url='http://m.520touxiang.com/touxiang/158531.html'
    while count<10:
        strhtml=requests.get(url)
        soup=BeautifulSoup(strhtml.text,'lxml')
        datas=soup.select("body > div.txtList > div.tx_content > img")
        for data in datas:
            picName=str(data.get("src"))
            pic=requests.get(picName)
            fName='pic/'+str(count)+'.jpg'
            f=open(fName,'wb')
            f.write(pic.content)
            f.close()
            count+=1
            if count==10:
                break
            print(count)
        datas=soup.select("body > div:nth-child(4) > ul > li:nth-child(2) > a")
        url='http://m.520touxiang.com'+str(datas[0].get("href"))
    print(time.time()-time1) 
    
        
    

    

if __name__=="__main__":
    main()
