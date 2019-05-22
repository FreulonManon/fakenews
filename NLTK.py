import nltk
import ssl
from nltk.corpus import wordnet as wn
from nltk.corpus import brown

from nltk.corpus import wordnet

#for ss in wordnet.synsets('chien', lang="fra"):
    #print(ss.name(), ss.lemma_names())



VERBE=[]
NOM=[]
ADJ=[]



texte = nltk.word_tokenize("And now for something completely different") 
result=nltk.pos_tag(texte)
for data in result: 
	

print(result)



#text = 'This is a table. We should table this offer. The table is in the center.' 
#text = nltk.word_tokenize(text) 
#result = nltk.pos_tag(text) 
#result = [i for i in result if i[0].lower() == 'table'] 

#print(result)





#from nltk.corpus import brown
#news_text = brown.words(categories='news')
#fdist = nltk.FreqDist([w.lower() for w in news_text]) In [136]: modals = ['can', 'could', 'may', 'might', 'must', 'will']
#for m in modals: