# EC601_Project2_TwitterAPI

In this part, there are 3 demos: TweetPosting Bot, TweetReplying Bot, and Get N tweets func.

You need to input your own API key, API key secret, ACCESS key, ACCESS key secret.

## 1.TweetPosting Bot
`TweetPostBot.py`

In this function, I used the `update_status` API to achieve tweets posting function. By running this program, we can randomly choose a segment from the sentence "Good morning, And in case I don't see you, Good afternoon, Good evening, And good night", and post it. 

Please notice that, twitter does not allow post the same content in a short time, so sometimes it might not work, if so, just change the content you are posting.

![f07ef4c962a4f1ee3fd3179c622bb4c](https://user-images.githubusercontent.com/90535023/141606927-1dbd84c5-d082-42bf-b750-89d360c7a48b.jpg)

## 2.TweetReplying Bot
`TwitterReplyBot.py`

This is a Twitter Auto Replying Bot, it can automatically find the tweet which @ it and with specif content: "#zjz"(or something else, you can change this), then reply it with: zjz. 

In this, I used `update_status`, `create_favorite`, `retweet` API to finish the work.

But TWITTER always shut it down or restrict it, I have no idea.

You need to input your own API key, API key secret, ACCESS key, ACCESS key secret.

I learnt it from Youtube Uploader: Certified Recaps.

There are still some small function mistakes, I might fixed it later.

## 3.Get N tweets func
`get_n_tweets.py`

In this, I use `user_timeline`, `wordcloud` API to get n tweets from specifc user, and generate the wordcloud picture of the tweets. This function is the basic of further Sentiment Analysis.

![image](https://user-images.githubusercontent.com/90535023/141607512-f2dfda71-5f1d-47cb-9a2a-0d2956d30ecb.png)
![Figure_1](https://user-images.githubusercontent.com/90535023/141607546-8435e390-806b-46df-898f-190687c3b9ee.png)

