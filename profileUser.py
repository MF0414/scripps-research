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

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, id=339998952).pages():
    #process followers
    ids.extend(page)

    #pause to avoid rate limit
    time.sleep(20)

print("User: 339998952\n") 
print("Total Followers: " + str(len(ids)) + "\n")
print(".........................................\n")

for i in range(20):
   print(str(i) + ". Follower ID: " + str(ids[i]))
   print("\nFriendship: " + str(api.show_friendship(target_id=339998952, source_id=int(ids[i]))))
   print("............................../n")
   print("\n")
