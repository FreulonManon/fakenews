import os
import csv
import requests
from bs4 import BeautifulSoup
requete = requests.get("https://zestedesavoir.com/tutoriels/?category=autres-informatique")
page = requete.content
soup = BeautifulSoup(page,features="html.parser")
h1 = soup.find("h1", {"class": "ico-after ico-tutorials"})
print(h1.string)
h3 = soup.find_all("h3", {"class": "content-title"})
desc = soup.find_all("p", {"class": "content-description"})

liste_titre = [elt.string.strip() for elt in h3]

liste_description = [elt.string.strip() for elt in desc]