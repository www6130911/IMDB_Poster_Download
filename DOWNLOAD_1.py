# -*- coding: utf-8 -*-

from string import digits
import imdb
import requests
import urllib.request
import csv
import pandas as pd
import json
import time
import os



headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }

with open('F:\IMDB_POSTER\links.csv','r',encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[1]for row in reader]
    imdbId = (column)




'''
#寻找电影ID
#MovieID
MoviePath = "https://www.imdb.com/find?ref_=nv_sr_fn&q="+name[1]
req = urllib.request.Request(MoviePath)
response = urllib.request.urlopen(req)
buff = response.read()
#显示
the_page = buff.decode("utf8")
response.close()
print(the_page)



'''






#url = "http://www.omdbapi.com/?i="+"tt"+str(imdbId[141])+"&apikey=bdf9ff4d"
#print(url)

# ---------------------------下载海报--------------------------------

    #access = imdb.IMDb()
    #movie = access.get_movie()
OMDb_API_Key = ['c009368a','867c2ab3','bdf9ff4d','7d5d8824','dfb2322','e117de50','85550c84','febcaabf','35f4d548',
                'a351853b','298a8037','aab1e0eb','1f664925','b696a3fd']

count = 0
j = 0
#for i in range(19561,27279): #上一次保存到这个数
for i in range(24403,25000):
    url = "http://www.omdbapi.com/?i="+"tt"+str(imdbId[i])+"&apikey="+OMDb_API_Key[count]
    #print(OMDb_API_Key[int((i+549)/1000)])
    #print(url)
    try:
        r = requests.get(url,headers,timeout = 3)
    except:
        print("TIME OVER")
        j = j + 1
        continue
    m = dict(r.json())
    #print(m)
    #print(m["Poster"])
    img_src = m["Poster"]
    if img_src=="N/A":
        print("N/A")
        j = j + 1
        continue

    #try:
    os.mkdir(r'F:/IMDB_POSTER/'+imdbId[i])
    #except FileExistsError :
     #   continue

    try:
        path = r"F:/IMDB_POSTER/"+imdbId[i]+"/"+imdbId[i]+".jpg"
        #print(path)
    except FileNotFoundError:
        print(m["Title"])
        j = j + 1
        continue
    time.sleep(1)
    try:
        urllib.request.urlretrieve(img_src,path)
    except OSError:
        print("OSError")
        j = j + 1
        continue
    except FileNotFoundError:
        print(m["Title"])
        j = j + 1

    except urllib.request.HTTPError as e:
        if e.reason == 404:
            print("404 error")
            j = j + 1
            continue
    except :
        print("Other Error")
        j = j + 1
        continue

    j = j + 1
    if j == 800:
        count = count +1
        j = 0
    print("i = %d, j = %d, count = %d"%(i , j ,count))

