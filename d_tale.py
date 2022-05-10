from bs4 import BeautifulSoup as bs
import requests
import urllib
import pandas as pd

def d_tale_2020():
    url = 'https://www.kongehuset.dk/nyheder/laes-hm-dronningens-nytaarstale-2020'
    
    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    d_tale_20=soup.find('div', class_='rich-text__container__content')
    
    cleaned_d_tale = [d_tale_20.get_text()]
    
    d_20 = pd.DataFrame(cleaned_d_tale)
    d_20.to_csv("d_tale_2020.csv")

    
def d_tale_2019():
    url = 'https://www.kongehuset.dk/nyheder/laes-hm-dronningens-nytaarstale-2019'

    response = requests.get(url)
    soup = bs(response.text,'html.parser')
    d_tale_19=soup.find('div', class_='rich-text__container__content')
    
    cleaned_d_tale = [d_tale_19.get_text()]
    
    d_20 = pd.DataFrame(cleaned_d_tale)
    d_20.to_csv("d_tale_2019.csv")

    

#d_tale_2020()
d_tale_2019()

