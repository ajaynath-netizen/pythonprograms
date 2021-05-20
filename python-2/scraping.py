import requests
from bs4 import BeautifulSoup

def scrape(url):
    r= requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    
    # a=[]
    # for i in x:
    #     a.append(i.contents)


    # y="\n".join(a)
    # return y
    return  soup.original_encoding
        

    
    #   r= requests.get(url)
    #   s=Beautifulsoup(r.text,"html.parser")
    

url="http://192.168.0.1/index.html"

print(scrape(url))