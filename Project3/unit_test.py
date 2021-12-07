import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

from testbook import testbook

@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)

# test for tweets number
def test_print(tb):
    print_tweets = tb.ref("print_tweets")
    
    # normal use cases
    assert print_tweets(10)==10
    assert print_tweets(100)==10
    assert print_tweets(5)==5
    assert print_tweets(11)==10
    
    # misuse case
    assert print_tweets(-1)==0
    assert print_tweets(0)==0
    assert print_tweets(2^2)==0
    assert print_tweets(50-10)==0
    
    # error handling
    assert print_tweets('one')=='Wrong Input!'
    assert print_tweets(ten)=='Wrong Input!'
    assert print_tweets('!@$')=='Wrong Input!'
    assert print_tweets([2])=='Wrong Input!'

    
@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)

# test for cleaning method
def test_clean(tb):
    cleanTxt = tb.ref("cleanTxt")
    
    # normal use cases
    assert cleanTxt('abc')=="abc"
    assert cleanTxt('@abc')==""
    assert cleanTxt('Lol#funny')=="Lolfunny"
    assert cleanTxt('#文字')=="文字"
    
    # misuse cases
    assert cleanTxt([abc])== #name 'abc' is not defined
    assert cleanTxt({abc})== # name 'abc' is not defined
    assert cleanTxt((@1+1))=='Wrong Input!'
    assert cleanTxt('@文字')== '@文字'
    
    # Error handling
    assert cleanTxt(123)== 'Wrong Input!'
    assert cleanTxt([10])== 'Wrong Input!'
    assert cleanTxt(print_tweets(10))=='1)@WorldAndScience If you leave hydrogen out in the sun long enough, it starts talking to itself /n Wrong Input!'
    assert cleanTxt(cleanTxt(123))== 'Wrong Input!'

# test for subjectivity score

@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)

def test_subj(tb):
    getSubjectivity = tb.ref("getSubjectivity")
    
    # normal use cases
    assert getSubjectivity('I love ECE')>0
    assert getSubjectivity('Love')==0.6
    assert getSubjectivity('dislike')==0
    assert getSubjectivity('I am who I am')==0
    
    # miseuse cases
    assert getSubjectivity('123456')==0
    assert getSubjectivity('!@#$')==0

    
    # error handling
    assert getSubjectivity(print_tweets(1))=='show the n recent tweets:

1)@WorldAndScience If you leave hydrogen out in the sun long enough, it starts talking to itself

please input text'
    assert getSubjectivity(cleanTxt('abc'))== EOL while scanning string literal
    assert getSubjectivity(I love ECE)== # invalid syntax

 #test for polarity score

@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)

def test_pola(tb):
    getPolarity = tb.ref("getPolarity")
    
    # normal use cases
    assert getPolarity('I am so sad')<0
    assert getPolarity('I am so happy')>0
    
    #Error handling
    assert getPolarity(print_tweets(1))=='show the n recent tweets:

1)@WorldAndScience If you leave hydrogen out in the sun long enough, it starts talking to itself

Wrong Input!'
    assert getPolarity(I am so happy)=='Wrong Input!'
    
    # misuse cases
    assert getPolarity('1234')==0
    assert getPolarity('!@#$')==0
  
