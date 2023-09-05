import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "MrqVnnY4sRsBpswn06k6RYYAH"
access_secret = "AvAJRJx5j7FBGbqpMwggMTJjwALDb7Nsj0CgTq4THnMzTz8784"
consumer_key = "966422530453057536-QG2IUjOZx5BAMdKLujmV2AyAnk3whWi"
consumer_secret = "ktpZdDu7E3fh6KEZSrqYSieGcb7bhGFWC7X2PiN2fIph1"

# Twitter auth
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           count = 200,
                           include_rts = False,
                           tweet_mode = 'extended')

print(tweets)