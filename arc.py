import arcpy
import json
import tweepy
import time
import csv
from tweepy.streaming import StreamListener


#Enter Twitter API Key information obtenu en créant une api twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
# céation d'un fichier csv pour stocker les données colléctées
with open("D:/VIGNERON/Output.csv", "w") as csvfile:
	file = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	file.writerow(['Nom_utilisateur'] + ['Date'] + ['Evenement'] + ['Source'] + ['Commune'] + ['Insee'] +['Localisation'] + ['Contenu'] + ['X'] + ['Y'])

data_list = []

count = 0
# entrez votre mot clé désiré
motcle = "Paris"

class StdOutListener(StreamListener):
	def on_status(self, status):
		json_data = status._json
		global count
# compteur à modifier selon votre désire
	if count <= 10 :
		coord = json_data["coordinates"]
# affichage des tweets seulement si ils possèdent une localisation
	if coord != None:
		user = status.user.name.encode('ascii', 'ignore').decode('ascii')
		print ("Nom d'utilisateur : " + user)
		date = str(status.created_at)
		print("Date de publication : " + str(status.created_at)) 
		evenement = "Innondation"
		print ("Evenement : " + evenement)
		source = "twitter"
		print ("source : " + source )
		commune = "Null"
		print ("Nom de la commune : " + commune)
		insee = "Null"
		print ("Code Insee commune : " + insee)
		localisation = "Null"
		print ("localisation : " + localisation)
		contenu = status.text.encode('ascii', 'ignore').decode('ascii')
		print("Tweet text: " + contenu)
		lon = coord["coordinates"][0]
		lat = coord["coordinates"][1]
		print ("Longitude : " + str(lon))
		print ("Latitude : " + str(lat))
#écriture des infos dans le fichier de sortie
	file = csv.writer(open("D:/VIGNERON/Output.csv", "a"), csvfile, delimiter=';' , quotechar='|' , quoting=csv.QUOTE_MINIMAL )
	file.writerow([user]+[date]+[evenement]+[source]+[commune]+[insee]+[localisation]+[contenu]+[lon]+[lat])

count += 1
	print count
return True
else :
	return False
file.close() 



def on_error(self, status_code):
	print('Got an error with status code: ' + str(status_code))
	return True # To continue listening

def on_timeout(self):
	print('Timeout...')
	return True # To continue listening


#connexion au flux twitter
listener = StdOutListener() 
stream = tweepy.Stream(auth, StdOutListener())
stream.filter(track=[motcle])

