import requests
import json
import random
import nltk
import ssl


from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk.corpus import wordnet


url='https://newsapi.org/v2/top-headlines?country=fr&apiKey=30274f542d134b74a8e47c88110d11e0'
data_raw = requests.get(url).json()  #articles récents
 
 
del data_raw["status"]
del data_raw["totalResults"]
 
articles = data_raw.get('articles')
#source=data_raw.get('source')
 
liste1 =[]
liste2 =[]
liste3=[]

texte = nltk.word_tokenize("And now for something completely different") 
result=nltk.pos_tag(texte)
#for data in result: 
	

print(result)


 
for data in articles:
    for key, value in data.items():
        if (key == 'title'):
        	if isinstance(value, str):
        		liste1.append(value)
        	else:
            	liste1.append("no data")
        elif(key=='content'):
        	liste2.append(value)
        elif(key=='publishedAt'):
        	liste3.append(value)


        
 
f = open('ARTICLES.txt','w') 
for i in range (len(liste1)):
    if (' ' in liste1[i]):
    	sourceliste = liste1[i].split(" ")
    	source = sourceliste[len(sourceliste)-1]
    	#print(liste2[i], type(liste2[i]))
	    #data = "JOURNAL: "+source+"\n"+"TITRE: "+liste1[i]+"\n"+"CONTENU: "+liste2[i]+"\n"+"DATE: "+liste3[i]+"\n\n\n"
	    #f.write(data)

#f.close()

#print(f)