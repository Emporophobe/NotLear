import random
import cPickle as pickle
import tweepy

#Tweepy setup

keys = [line.rstrip('\n') for line in open('twitterkeys.txt')]

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY = keys[2]
ACCESS_SECRET = keys[3]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Prepare the database

corpus = 'shakespeare'
database = pickle.load(open(corpus+'.p'))

#generate a sentence

def generate():
    seed = database.keys()[random.randint(0, len(database.keys())-1)]
    gentext = []
    endpunct = ['.', '?', '!']

    while len(gentext) < 100:
        gentext.append(seed[0])
        try:
            new = database[seed][random.randint(0, len(database[seed])-1)]
        except:
            new = database[seed][random.randint(0, len(database[seed])-1)]
            
        seed = (seed[1], new)
        
    while len(gentext) > 1:
        if gentext[1][0].isupper() and gentext[0][-1] in endpunct:
            gentext.pop(0)
            break
        else:
            gentext.pop(0)

    sentence = []

    for word in gentext:
        if word[-1] not in endpunct:
            sentence.append(word)
        else:
            sentence.append(word)
            break

    text = ' '.join(sentence)
    text = text.replace('\x97', '--') #replace em dashes with double hyphens

    return text
        
def maketweet():
    try:
        line1 = generate()
    except (IndexError, KeyError):
        maketweet()
    
    while len(line1) < 15 or line1.isupper():
        line1 = generate()

    tweet = line1

    if len(line1) < 140:
        line2 = generate()
        
        while len(line2) < 15 or line2.isupper():
            line2 = generate()

        if len(line1 + line2) < 140:
            tweet = line1 + ' ' + line2
        
    if  len(tweet) <= 140 and len(tweet) >= 15 and tweet.isupper() == False and tweet[-1] in ['.', '?', '!']:
        return tweet
    else:
        return maketweet()

x = maketweet()
print x
api.update_status(x)

