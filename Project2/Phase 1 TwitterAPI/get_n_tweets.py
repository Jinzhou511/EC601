# import
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

# You need input your own key and secret
twitter_auth_keys = {
    "consumer_key"        : "JR6B8K1QWpYeMqMKYAiGkIF3l",
    "consumer_secret"     : "A83zp1kFCtrBTNmpwNnxXWRLRTsSshmRkRkl9MV29Bu7DYkBZm",
    "access_token"        : "1393886621729271815-MSUMYiX5E7dOqv688WtlRDL861LVEg",
    "access_token_secret" : "kRPXGNrEecnKUTg1n0Xm4nxFQ22loyuoKkFdbjzSYdskM"
}

# Authorization part
auth = tweepy.OAuthHandler(twitter_auth_keys['consumer_key'],twitter_auth_keys['consumer_secret'])
auth.set_access_token(twitter_auth_keys['access_token'],twitter_auth_keys['access_token_secret'])
api = tweepy.API(auth)

# get N tweets 
posts = api.user_timeline(screen_name='BillGates',count=10,lang="en",tweet_mode="extended")
print("show the n recent tweets:\n")
i = 0
for tweet in posts[0:10]:
    i+=1
    print(str(i)+')'+tweet.full_text+'\n')

df = pd.DataFrame([tweet.full_text for tweet in posts],columns=['Tweets'])

def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+','',text)
    text = re.sub(r'#','',text)
    text = re.sub(r'RT[\s]+','',text)
    text = re.sub(r'https:\/\/S+','',text)
    return(text)

# word cloud
allWords = ' '.join([twts for twts in df['Tweets']])
wordCloud = WordCloud(width = 500,height = 300, random_state=80, max_font_size=100).generate(allWords)
plt.imshow(wordCloud,interpolation='bilinear')
plt.axis('on')
plt.show()
