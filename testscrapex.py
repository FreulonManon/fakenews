from bs4 import BeautifulSoup
import requests
from random import *
#url='https://www.lemonde.fr/'

def site(url):
	result=requests.get(url)
	content = result.content
	soup = BeautifulSoup(content, features="html.parser")
	return(soup)
#balise=('p')


def fichier(texte, balise):

	for p in texte.find_all(balise):
		fichier = open("data.txt", "w")
		resultat=p.text
		fichier.write(resultat)
		fichier.close()


def balisechoice(url,balise):
	texte=site(url)
	fichier(texte, balise)	

if __name__=="__main__":
	url=input("url du site:")
	balise=input("balise:")
	balisechoice(url, balise)

	

    
#for h in soup.find_all(titre):
	#print(h)
 
#for i, n in enumerate(texte):
#	resultat = texte[i].find('p').text
#	fichier = open("data.txt", "a")
#	fichier.write(resultat)
#	fichier.close()

 

#<p class='article_desc'>
#<h1 class='article_title'>