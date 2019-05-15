import requests
from bs4 import BeautifulSoup

url =' https://www.lemonde.fr/international/article/2019/05/03/les-deux-grands-partis-britanniques-sanctionnes-dans-les-urnes_5457735_3210.html'
result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, features="html.parser")

date=soup.find_all(class_='meta_publisher')


LEMONDE= date.find_all(class_='meta_publisher').text
file= open('LEMONDE.txt', 'w', encoding='utf-8')
file.write(resultat)
file.close()



   # resultat = date[i].find(class_='meta_publisher').text
    #file = open('resultat.txt', 'a', encoding='utf-8')
    #file.write(resultat)
   # file.close()

	