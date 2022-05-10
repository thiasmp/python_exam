from bs4 import BeautifulSoup as bs
import requests
import urllib
import pandas as pd

def s_tale_2020():
    url = 'https://www.regeringen.dk/aktuelt/statsministerens-nytaarstale/mette-frederiksens-nytaarstale-1-januar-2020/'

    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    s_tale_20=soup.find('section', class_='component richtext')
    stripped_s_tale = []
    
    cleaned_s_tale = [s_tale_20.get_text()]
    for e in cleaned_s_tale:
        stripped_s_tale.append(e.replace("\n","").replace("*",""))
        
    
    s_20 = pd.DataFrame(stripped_s_tale)
    s_20.to_csv("s_tale_2020.csv")
    

def s_tale_2019():
    url = 'https://www.regeringen.dk/aktuelt/statsministerens-nytaarstale/lars-loekke-rasmussens-nytaarstale-1-januar-2019/'

    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    s_tale_19=soup.find('section', class_='component richtext')
    stripped_s_tale = []
    
    cleaned_s_tale = [s_tale_19.get_text()]
    for e in cleaned_s_tale:
        stripped_s_tale.append(e.replace("\n","").replace("*",""))
        
    
    s_19 = pd.DataFrame(stripped_s_tale)
    s_19.to_csv("s_tale_2019.csv")
    
s_tale_2019()        
#s_tale_2020()    