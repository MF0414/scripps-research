#"user":{"id":339998952,"id_str":"339998952","name":"Jammies Jons","screen_name":"JJGutierrez09","location":"Panama City, FL"


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time


access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

u = api.get_user(screen_name = 'GVSU')
gloire = api.get_user(screen_name = 'GloireKnowsBest')
GVSU_ID = u.id
gloire_ID = gloire.id
i = 0
ids = []
page = tweepy.Cursor(api.followers_ids, screen_name='@GVSU').pages()


friendship = api.show_friendship(target_id=GVSU_ID, source_id=gloire_ID)

print(friendship[1])
