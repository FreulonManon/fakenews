from random import *
#theme = ["gilets jaunes", "attentat", "immigration", "sport", "brexit", "climat"]
#N=choice(theme)
#choisi=[]
#choisi.append(N)
#print(choisi)

import requests
import json


url='https://newsapi.org/v2/everything?sources=le-monde&apiKey=30274f542d134b74a8e47c88110d11e0'
data_raw = requests.get(url).json()  #articles récents
# data= r.json()

# for key in data_raw:
# 	print(key)

articles = data_raw.get('articles')

titles = {}


for data in articles:
	for key, value in sorted(data.items()):
		if key == 'title':
			titles.append(value)
			#title.append(data.get('title'))


for title in titles:
		
	print(titles)

# with open("test.json", "w") as file:
# 	json.dump(data, file, ensure_ascii=False, indent=4)
#for h in soup.find_all(data):	
#	print (h)
# 	resultat=h.text
# 	fichier.write(resultat)

# fichier.close()
# print(data)














