#Author: Michael Foster
#Description: This code harvests the twitter users who follow GVSU
#             assigns them a simple id value and stores them into a 
#             comma-delimited text file.


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time
import json

def export_followers(id_list):

   new_id = 0
   FILE = open('follower_ids.txt', "w")
   FILE.write("user,id\n")
   for user in id_list[0]:
      FILE.write(str(user))
      line = "," + str(new_id)
      FILE.write(line)
      FILE.write('\n')
      new_id = new_id + 1
   FILE.close()

if __name__ == '__main__':
   
   #API Setup
   access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
   access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
   consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
   consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"

   auth = OAuthHandler(consumer_key, consumer_secret )
   auth.set_access_token(access_token, access_token_secret)

   api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

   #Grab GVSU Followers
   u = api.get_user(screen_name = 'GVSU')
   GVSU_ID = u.id
   i = 0
   ids = []
   page = tweepy.Cursor(api.followers_ids, id=GVSU_ID).pages()

   print("Listening..")
   run = True
   while run == True:
      try:
         
         #process followers
         ids.extend(page)
         print("Gathering ID: ", str(i + 1))
         i = i + 1
         if i == 46358:
            run = False
      except tweepy.TweepError:
         #pause to avoid rate limit
         time.sleep(60 * 15)
         continue
      except StopIteration:
         break

   export_followers(ids)
