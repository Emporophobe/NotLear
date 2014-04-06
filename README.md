NotLear
=======

Markov Chains + Shakespeare + Twitter

This program uses Markov Chains to create unique tweets based upon the four great tragedies of William Shakespeare.

https://twitter.com/NotLear

Installation
============
NotLear requires Python 2.7, the Tweepy module, and a Twitter account with developer credentials to post to Twitter. Get Tweepy from https://github.com/tweepy/tweepy and install it first. Visit https://dev.twitter.com/ to set up your developer credentials and create a new application with both read and write permissions.

Download the repo to a single directory. You must also create a .txt file named twitterkeys.txt in which you put, one per line:

  API key, 
  API secret, 
  Access Token, 
  Access Token Secret

This should only contain the keys, without punctuation etc.

Running
=======
After you have everything downloaded into one directory, simply run notlear.py and, if you want the account to reply to mentions, also run reply.py. Currently, notlear.py will post once every 4 hours, with extra tweets in reply to mentions if reply.py is running.

Alterations
==========
If you want to change the corpus (source text, determines the style of the output text), find a .txt file that contains your new corpus. Place it in the NotLear directory. Run pickler.py, and input the name of your text file when prompted. This will generate a pickle (.p) file that should be several times larger than the text file. This may take several minutes to complete. Next edit NotLear.py, changing the variable 'corpus' from 'shakespeare' to the name of your text file. 

The other main variable is the time between tweets, found as the argument of time.sleep(seconds). Changing this from the default of 14400 seconds (4 hours) will change the frequency of tweets. Keep in mind there is a limit to the number of tweets per day.

Sources
========
  Hamlet
  King Lear
  Macbeth
  Othello
  
Source text from Project Gutenberg (http://www.gutenberg.org)
