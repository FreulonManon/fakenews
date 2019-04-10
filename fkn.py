import requests
import json
from random import*

theme = ["jaunes", "gilets", "sport", "brexit", "climat"]
N=choice(theme)
choisi=[]
choisi.append(N)
print(choisi)
 
f = open('ARTICLES.txt','w')
 
url='https://newsapi.org/v2/everything?sources=le-monde&apiKey=30274f542d134b74a8e47c88110d11e0'
data_raw = requests.get(url).json()  #articles récents
 
 
del data_raw["status"]
del data_raw["totalResults"]
 
articles = data_raw.get('articles')
 
liste1 =[]
liste2 =[]
 
for data in articles:
    for key, value in data.items():
        if (key == 'title'):
            liste1.append(value)
        elif(key=='content'):
            liste2.append(value)
 
 
for i in range (len(liste1)):
    if ('jaunes' in liste1[i]):
        f.write("TITRE : "+liste1[i]+"\n"+"CONTENU : "+liste2[i]+"\n\n\n")
f.close()


print(f)