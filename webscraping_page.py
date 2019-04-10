import requests

url = 'https://www.lemonde.fr/economie/article/2019/02/23/comment-bruxelles-prepare-l-europe-au-no-deal_5427295_3234.html'
result = requests.get(url)
print(result.content)