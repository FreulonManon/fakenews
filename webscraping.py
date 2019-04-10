from bs4 import BeautifulSoup
import requests
from random import *
url = 'https://www.lemonde.fr/economie/article/2019/02/23/comment-bruxelles-prepare-l-europe-au-no-deal_5427295_3234.html'
result = requests.get(url)
result
content = result.content
soup = BeautifulSoup(content, features="html.parser")
soup
#theme = ["gilets jaunes", "attentat", "immigration", "sport", "brexit", "climat"]
#N=choice(theme)
##choisi.append(N)
#print(N)
date = soup.find_all(class_='meta_publisher')
titre=soup.find_all(class_='article_title')
texte=soup.find_all('p')
auteur=soup.find_all(class_='meta_author')

for i, p in enumerate(date):
    resultat = date[i].find(class_='meta_publisher').text
    file = open('resultat.txt', 'a', encoding='utf-8')
    file.write(resultat)
    file.close()


from time import sleep
from time import time
from random import randint
from warnings import warn
def get_res(url , max_num):
    
    pages = [str(i) for i in list(range(1, max_num))]
    
    data = []
    
    print('start get {}'.format(url))
    
    for page in pages:
        requetes = 0
        start_time = time()
        response = requests.get(url + 'page/' + page)
        sleep(randint(8, 15))
        requetes += 1
        elapsed_time = time() - start_time
        
        print('status {}, page {}, requetes {}'.format(response.status_code, page, requetes))
        
        if response.status_code != 200:
            warn('status {}, page {}, requetes {}'.format(response.status_code, page, requetes))
            continue
            
        if requetes > 50:
            break
            
        data.append(response.content)
    
    print('scrap {} end'.format(url))
    
    return(data)
    pages = get_res(url, 81)