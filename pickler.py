import random
import cPickle as pickle

def getCorpus():
    corpus = raw_input("Corpus text: ")
    if len(corpus) < 4 or corpus[-4] == '.':
        corpus = corpus[0:-4]
    try:
        return open(corpus+'.txt', 'r'), corpus
    except IOError:
        print 'No such .txt file. Try again.'
        getCorpus()

text, corpus = getCorpus()

wordlist = text.read().split()
database = {}

for i in range(len(wordlist)-2):
    w1, w2, w3 = (wordlist[i], wordlist[i+1], wordlist[i+2])
    key = (w1, w2)
    if key in database.keys():
        database[key].append(w3)
    else:
        database[key] = [w3]
pickle.dump(database, open(corpus+'.p', 'w'))  
