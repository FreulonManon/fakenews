import requests
from bs4 import BeautifulSoup
import json
import os

class LesNumeriques(object):
	
	def __init__(self):
		self.domain = 'https://www.lesnumeriques.com'
		self.url = self.domain + '/actualites'
		
	def getData(self):
		html = requests.get(self.url).text
		self.soup = BeautifulSoup(html, 'lxml')

	def parseList(self):
		listActu = self.soup.find('ul', {'class': 'list-content'})
		actualites = []

	
		for actu in listActu.find_all('li', {'class': 'news'}):
				actualite = {}

		
				actualite['lien'] = self.domain + (actu.find('a')['href']
		
		
				actualite['titre'] = (actu.find('h2').text
				actualite['accroche'] = (actu.find('div', {'class': 'subtitle'}).text
				actualite['resume'] = (actu.find('div', {'class': 'text'}).text
				actualite['heure'] = (actu.find('div', {'class': 'item-date'}).text
				actualites.append(actualite)

		return actualites

		if __name__ == '__main__':
			ln = LesNumeriques()
	
			ln.getData()
			parsedJson = json.dumps(ln.parseList())
			print(parsedJson)

	def cleanHTML(self, data):
			props = ['Lire la suite', '\t', '\n', '\r', '    ']
			for p in props:
					data = data.replace(p, '')

			return data