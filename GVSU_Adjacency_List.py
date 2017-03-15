from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time
import json


def extract_friendship(friend_object):
   if "followed_by=True" in str(friend_object[1]):
      return True
   else:
      return False


if __name__ == '__main__':

#API Setup
   access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
   access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
   consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
   consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"

   auth = OAuthHandler(consumer_key, consumer_secret )
   auth.set_access_token(access_token, access_token_secret)

   api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

#ID Extraction
   id_tuples = []

   with open("follower_ids.txt") as f:
      content = f.readlines()
   content = [x.strip() for x in content]

   for item in content:
      id_tuples.append(item.split(','))

#Build Friendship Adjacency List
    
   id_tuples.remove(["user","id"]) #Remove header
   n = len(id_tuples)
   network = {}
   
   for i in range(n - 1):
      target = int(id_tuples[i][0])
      target_mapped = int(id_tuples[i][1])
      for j in range(n):
         source = int(id_tuples[j][0])
         source_mapped = int(id_tuples[j][1])
         followers = []
         print("Fetching " + str(target_mapped) + " , " + str(source_mapped)) 
         if extract_friendship(api.show_friendship(target_id=target, source_id=source)):
            followers.append(source_mapped)
      network[target_mapped] = followers

#Store Network Adjacency Dictionary into File
   print("Sending Network to File")
   with open('GVSU_Twitter_Network.json','w') as o:
      json.dump(dictionary,o)

   
