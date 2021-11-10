# Project2 
In this dict, there are three parts:TwitterAPI, GoogleNLP, and Sentiment Analysis.
## Phase 1
### · Twitter API

I wrote 3 demos for twitter API. 

* The first one is `TweetPostBot.py`, which can randomly choose a sentence from the <The Truman Show>'s lines 'Good morning, and in case I don't see you, good afternoon, good evening, and good night!' and post it.
        ![f07ef4c962a4f1ee3fd3179c622bb4c](https://user-images.githubusercontent.com/90535023/141172950-a9aefdc7-1ffe-4469-8755-db26979fdf04.jpg)

  
* The second one is `TwitterReplyBot.py`, it can automatically find the tweet which @ the Bot with specif content: "#zjz" (or something else, you can change this), then reply it with: zjz.
  
* The third one is `get_n_tweets.py`, this func can automatically get n tweets(the number is set in the program) from one specific user(also set in program) and plot a wordcloud,such as get 100 tweets from Bill Gates, get 50 tweets from Elon Mask. This is for the preparation of next phase, the tweets this func get can be used for sentiment analysis.
        ![image](https://user-images.githubusercontent.com/90535023/141173233-b690bed8-b009-47af-9d08-29a7e6f63bc3.png)
        ![image](https://user-images.githubusercontent.com/90535023/141173366-850d90ee-0b40-4405-b1c7-ea82d00ce848.png)


### · Google NLP

* In this phase, I chose a google NLP model and input the csv data into the model, the uploading and training took a very long time, about several hours.
After training, we can input any word or sentence into test window, and this would tell us the emotion feature of the word.
  
## Phase 2
### · Sentiment Analysis
* In this project, I used Twitter API and Sentiment Analysis tools to:

① Get a specified number of tweets from a specified user. In this case, I choose JoeBiden to be the analyzed user.

② Filter unimportant information such as symbols and numbers in the obtained tweets.

③ Calculate the subjectivity and polarity of each tweet, and give the sentiment.

④ Plot the plane distribution of polarity and subjectivity.
