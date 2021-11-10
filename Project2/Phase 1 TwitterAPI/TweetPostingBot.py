import tweepy
 
def main():
    # You need input your own key and secret
    twitter_auth_keys = {
        "consumer_key"        : "xxxx",
        "consumer_secret"     : "xxxx",
        "access_token"        : "xxxx",
        "access_token_secret" : "xxxx"
    }
    
    # Authorization part
    auth = tweepy.OAuthHandler(twitter_auth_keys['consumer_key'],twitter_auth_keys['consumer_secret'])
    auth.set_access_token(twitter_auth_keys['access_token'],twitter_auth_keys['access_token_secret'])
    api = tweepy.API(auth)
 
    # You need type in different messages every time,
    # because twitter doesn't allow posting same tweets in a short time
    tweet = "Twitter postingBot is now posting a tweet!"
    status = api.update_status(status=tweet)
 
if __name__ == "__main__":
    main()
