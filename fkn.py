import requests
import json
import random
import nltk
import ssl
import re
from random import *
from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk.corpus import wordnet

#https://newsapi.org/v2/top-headlines?country=fr&apiKey=30274f542d134b74a8e47c88110d11e0
url='https://newsapi.org/v2/top-headlines?country=gb&apiKey=30274f542d134b74a8e47c88110d11e0'
data_raw = requests.get(url).json()  #articles récents
 
 
del data_raw["status"]
del data_raw["totalResults"]
 
articles = data_raw.get('articles')
#source=data_raw.get('source')
 
liste1 =[]
liste2 =[]
liste3=[]

VERBE=[]
NOM=[]
DETER=[]
IN=[]
PHRASE=[]









for data in articles:
    for key, value in data.items():
        if (key == 'title'):
            if isinstance(value, str):
            	liste1.append(value)
            else:
                liste1.append("no data")
        elif(key=='content'):
            if isinstance(value, str):
                	liste2.append(value)
            else:
                liste2.append("no data")
        elif(key=='publishedAt'):
            if isinstance(value, str):
                	liste3.append(value)
            else:
                liste3.append("no data")


for l in liste2:
    texte=(nltk.word_tokenize(l))
    result=nltk.pos_tag(texte)



    
for r in result:
	if r[1] == 'NN':
		NOM.append(r[0])
	if r[1] == 'NNP':
		NOM.append(r[0])
	if r[1] == 'VB':
		VERBE.append(r[0])
	if r[1] == 'VBZ':
		VERBE.append(r[0])
	if r[1] == 'VBP':
		VERBE.append(r[0])
	if r[1] == 'VBN':
		VERBE.append(r[0])
	if r[1] == 'DT':
		DETER.append(r[0])
	if r[1] == 'IN':
		IN.append(r[0])


   


D=choice(DETER)
PHRASE.append(D)

N=choice(NOM)
PHRASE.append(N)

V=choice(VERBE)
PHRASE.append(V)

I=choice(IN)
PHRASE.append(I)

D=choice(DETER)
PHRASE.append(D)

N=choice(NOM)
PHRASE.append(N)

p= open('PHRASES.txt', 'a')
p.write(PHRASE)
p.close()
#print(PHRASE)


"""
prendre la chaine de liste2
tokenization + postag
reconstituer des titres d'articles aléatoirement
determinant un verbe un nom
"""
        
 
f = open('ARTICLES.txt','a') 
for i in range (len(liste1)):
    if (' ' in liste1[i]):
        sourceliste = liste1[i].split(" ")
        source = sourceliste[len(sourceliste)-2]
        data = "JOURNAL: "+source+"\n"+"TITRE: "+liste1[i]+"\n"+"CONTENU: "+liste2[i]+"\n"+"DATE: "+liste3[i]+"\n\n\n"
        f.write(data)

f.close()
