import requests
import time
import json
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime

# там самое главное не парсить все это добро примерно с 14:00 до 06:00 утра по Москве
 
data_list={}
url = "https://ghsecurities.bluematrix.com/sellside/Disclosures.action"

headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":f"{ UserAgent().random}",
    }
proxies ={
    'https':f'http://cHQj8c:g40BhE@192.241.122.251:8000'   
    }

def run(start,end):   
         
    session= requests.Session()
    session.get(url=url)
    
    with open("collection.json","r") as file:
        collections = json.load(file)
    
        for i in range(0,len(collections))[start:end]:
    
            p= session.post(url=url,headers=headers,proxies=proxies,data=get_data_in_collection(i))
            
            try:
                data= execute(p)   
                post(data=data)             
            except:
                print("Skip")
                
        print(p.status_code)
            
    print("Success")
    pass

def get_collection():
    
    # with open('index.html','r') as file:
    #     responce = file.read()   
    
    responce = requests.get(url=url,headers=headers,proxies=proxies)
        
    collection = []     
    soup = BeautifulSoup(responce.text,'lxml')
    values = soup.find_all("option")
    for value in values:
        print(value.text.strip())
                
        collection.append({        
            "ajax":"",
            "page":"ajax/simpleSearchInfoNew.jsp",
            "id":value["value"],
            "firmId":"19614",
        })
        
    
    with open ("collection.json", "w")as file:
        json.dump(collection,file,indent=4,ensure_ascii=False) 
    
def get_data_in_collection(index):
    
    with open("collection.json","r") as file:
        d = json.load(file)
        
    return d[index]    
  
def execute(responce):
    # with open("post.html","r") as file:
    #     src = file.read()
            
            
    soup = BeautifulSoup(responce.text,"lxml")
    
    
    ########################################################
   
    tiket = soup.find("tr").text
    tiket= tiket.replace("Disclosures for company"," ")
    tiket= re.sub(r'\s+', ' ', tiket) # убрать лишние пробелы   
   
    
    ########################################################
    #if soup.find("b",string=re.compile("Risks")):                
    risks = ""
    
                
    risks_elements = soup.find("b",string=re.compile("Risks")).find_parent("tr").find_next("tr").find_all("p")

    if len(risks_elements)<=0:
        risks_elements = soup.find("b",string=re.compile("Risks")).find_parent("tr").find_next("tr").find_all("li")
             
    for r in risks_elements:
        risks += f"{r.text}\n"
    ########################################################
    
    price = ""
    price_elements = soup.find("b",string=re.compile("Price Target")).find_parent("tr").find_next("tr").find_all("p")
    for p in price_elements:
        price += f"{p.text}\n"
    
    scrap_time = datetime.datetime.now().strftime("%d:%m:%Y %H:%M")
    
    data_list[tiket] = {
        "Source":"bluematrix.com",
        "Risks" :risks,
        "Price":price,        
    }    
    
    #return data
    
def post(data):
    with open("data2.json","a",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False) 
      
    
    
    
    
    

if __name__ == "__main__": 
    start = time.time()
       

    #run(0,510)
    get_collection()
    # with open("collection.json","r") as file:
    #     collection =  json.load(file)
        
    # print(len(collection))
    #print(get_data_in_collection(4))
    #print( execute())
    print(time.time()-start)
        
            