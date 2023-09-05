import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    access_key = "MrqVnnY4sRsBpswn06k6RYYAH"
    access_secret = "AvAJRJx5j7FBGbqpMwggMTJjwALDb7Nsj0CgTq4THnMzTz8784"
    consumer_key = "966422530453057536-QG2IUjOZx5BAMdKLujmV2AyAnk3whWi"
    consumer_secret = "ktpZdDu7E3fh6KEZSrqYSieGcb7bhGFWC7X2PiN2fIph1"

    # Twitter auth
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Create API object
    api = tweepy.API(auth)

    user_ids = ['bmcd243', 'elonmusk', 'Alphail','Authention','Beater','BoaJoy','CrescentSosa','CriticRee','Doctorni','EverBoard','Gambitch','Goden','HeroStronger','Holesoft','Knightsw','Kyousess','Melentum','MercyMessage','Pacyh','PurfectChosen','SimpleRocker','Sraer','Sublimar','Swortchs','Tarylh','TrippinPrank','TwinkleCent','Viglercy','WilBeauty','Wundersi','Wycomah','YouVander']

    users = api.lookup_users(screen_name=user_ids)


    users_list = []

    for user in users:
        refined_info = {"user_id": user.id,
                        'screen_name': user.screen_name}
        
        users_list.append(refined_info)

    df = pd.DataFrame(users_list)
    df.to_csv("s3://bmcd243-airflow-bucketInfo/user_details.csv")
