# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 23:20:18 2018

@author: Eric
"""
import requests
from bs4 import BeautifulSoup
import threading
from pytube import YouTube
from time import sleep
import os

def download(url):
    yt = YouTube(url)
    yt.streams.first().download("華語流行音樂")
    
rootUrl = "https://www.youtube.com"

#舊連結
videoUrl = "清單影片網址"

if not os.path.exists("華語流行音樂"):
    os.mkdir("華語流行音樂")

for page in range(386):
    res = requests.get(videoUrl)
    soup = BeautifulSoup(res.text,"html.parser")
    
    tagName = "div div div a"
    arti = soup.select(tagName)
    
    for i in range(len(arti)):
        try:
            if arti[i]['title'] == "下一部影片":
                while threading.active_count() > 14:
                    print("目前執行續數量： " + str(threading.active_count()))
                    print("目前下載到第 " + str(page) + "部影片")
                    sleep(20)
                    
                url = rootUrl + arti[i]['href']
                
                t = threading.Thread(target=download,args=(url,))
                t.start()
                
                videoUrl = url
                
        except:
            pass