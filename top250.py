 # -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:17:53 2018

@author: Root
"""

import requests
from bs4 import BeautifulSoup 
import pandas as pd

def one_page_top(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    top = []
    for i in soup.select('.info .bd'):
        text = i.select("p")[0].text.split("/")[-1].strip()
        top.append(text)
    return top

def all_page_top(url):
    all_top=[]
    for i in list(range(0,251,25)):
        a = one_page_top(url.format(i))
        all_top.extend(a)
    return all_top

def df_data(data):
    all_a_text = []
    
    for i in data:
        a = i.split(" ")
        all_a_text.extend(a)
    topic = list(set(all_a_text))
    result={}
    for i in topic:
        result[i] = all_a_text.count(i)
        df_result = pd.DataFrame.from_dict(result,orient='index').T
    return df_result,topic

if __name__ == "__main__":
    url = "https://movie.douban.com/top250?start={}&filter="
    all_a = all_page_top(url)
    df,topic= df_data(all_a)

from pyecharts import Bar
bar = Bar("电影TOP250电影分类", "爬取于豆瓣电影")
bar.add("电影分类", topic, df.ix[0,:], is_label_show=True,xaxis_interval=0 ,xaxis_rotate=45,
        is_datazoom_show=True,datazoom_type='both',mark_point=["max", "min"])
bar.render()  
    
    
    
    
    
    
    
    
    
    
    
    
    
