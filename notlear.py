#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import cPickle as pickle
import tweepy
import time

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

#Generate a single sentence
    
def generate(words):
    seed = database.keys()[random.randint(0, len(database.keys())-1)]
    gentext = []
    endpunct = ['.', '?', '!']
    
    while len(gentext) < int(words):
        gentext.append(seed[0])
        try:
            new = database[seed][random.randint(0, len(database[seed])-1)]
        except KeyError:
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

#Generate a sentence or two, all less than 140 characters

def maketweet():
    try:
        line1 = generate(100)
    except (IndexError, KeyError):
        maketweet()
    
    while len(line1) < 15 or line1.isupper():
        line1 = generate(100)

    tweet = line1

    if len(line1) < 140:
        line2 = generate(100)
        
        while len(line2) < 15 or line2.isupper():
            line2 = generate(100)

        if len(line1 + line2) < 140:
            tweet = line1 + ' ' + line2
        
    if  len(tweet) <= 140 and len(tweet) >= 15 and tweet.isupper() == False and tweet[-1] in ['.', '?', '!']:
        return tweet
    else:
        return maketweet()
        
while True:
    x = maketweet()
    print x
    print
    api.update_status(x)
    time.sleep(14400)
