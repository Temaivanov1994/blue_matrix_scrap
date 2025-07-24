import requests
import time
import json
import re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime
import aiohttp
import asyncio

# там самое главное не парсить все это добро примерно с 14:00 до 06:00 утра по Москве
active = True 
data_list={}
time_between_run = 20
url = "https://ghsecurities.bluematrix.com/sellside/Disclosures.action"

headers = {
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":f"{ UserAgent().random}",
    }
proxy =f'http://cHQj8c:g40BhE@192.241.122.251:8000'   

proxies ={
    'https':f'http://cHQj8c:g40BhE@192.241.122.251:8000'   
    }

def get():
    with open("async_data.json","r") as file:
        data = json.load(file)
        
    return data    
    

async def run():
    
    collections_count= await get_collection()
    
    #with open("collection.json","r") as file:
    #    collections_count = json.load(file)
    
    async with aiohttp.ClientSession() as session:
        tasks =[]
        
        count = int(len(collections_count))
        step = int(count/40)
        s = 0 
        e = 0 
        for i in range(0,count,step):
            e = i + step
            if e > count:
                e =count 
            s = i    
            task = asyncio.create_task(get_tiket_data(session, s,e))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
    
    with open("async_data.json","w",encoding="utf-8") as file:
        json.dump(data_list,file,indent=4,ensure_ascii=False)
    
    return

async def get_tiket_data(session,start,end):   
           
    for i in range(start,end):        
        async with session.post(url=url,headers=headers,proxy=proxy ,data=get_data_in_collection(i)) as responce:
            responce_text = await responce.text()
            try:
                await execute_data(responce_text)               
            except:
                continue
                
    print(f"Complite get_tiket_data({start} {end}) ")
            
   
    pass

async def get_collection():
    
    # with open('index.html','r') as file:
    #     responce = file.read()   
    
    responce = requests.get(url=url,headers=headers,proxies=proxies)
        
    collection = []     
    soup = BeautifulSoup(responce.text,'lxml')
    values = soup.find_all("option")
    for value in values:
        #print(value.text.strip())
                
        collection.append({        
            "ajax":"",
            "page":"ajax/simpleSearchInfoNew.jsp",
            "id":value["value"],
            "firmId":"19614",
        })
        
    
    with open ("collection.json", "w")as file:
        json.dump(collection,file,indent=4,ensure_ascii=False) 
    
    return collection
    
    
def get_data_in_collection(index):
    
    with open("collection.json","r") as file:
        d = json.load(file)
        
    return d[index]    
  
async def execute_data(responce_text):
    # with open("post.html","r") as file:
    #     src = file.read()
            
            
    soup = BeautifulSoup(responce_text,"lxml")
    
    
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
        "Tiket":tiket,
        "Risks" :risks,
        "Price":price,       
    }    
    
   # return data
    
async def post(data):
           
    with open("data.json","a") as file:
        json.dump(data,file,indent=4,ensure_ascii=False) 
 

async def update():
    while(active):
        
        print("sleep")
        await asyncio.sleep(20)
        task1 = asyncio.create_task(run()) 
        await task1 
        print ("Update")   
    
    # schedule.every(10).seconds.do(asyncio.run(run))
    # while active:
    #     schedule.run_pending()
       


if __name__ == "__main__":     
    asyncio.run( update())
    
        
            