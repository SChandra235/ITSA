# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:55:13 2018

@author: ImBidExter
"""

# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import twython
import tweepy
import twitter
from mtranslate import translate

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()
api = twitter.Api(consumer_key='RuuPbFVWoDLw5dg7Ib7Bfvww5',
  consumer_secret='YxETYSCDbFQ3Zn5be2biN0fbXj4WnKJn5QPr8TCz8zQgjL5DwG',
  access_token_key='2351340067-4i9oqFneGEdxydryj99n5TJDiJcUK7nvcoU3wP0',
  access_token_secret='s7xp1e5y7uqzjqsFN9t3vyvsDTr9Kw3O33nRAckK4mFqg')
#help(api.GetUserTimeline)
t = api.GetUserTimeline(screen_name="SrBachchan", count=20)
tweets = [i.AsDict() for i in t]
for t in tweets:
    print(translate(t['text'],'en'))
    #print(gs.translate(t['text'],'en').translate(non_bmp_map))
    #print(t['text'])
    # Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
    #scores = sid.polarity_scores(t['text'])
    scores = sid.polarity_scores(translate(t['text'],'en'))
    # Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen
    for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')
        print()
