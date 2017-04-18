#!/usr/bin/python3.4

# Listens for tweets from GVSU followers
#@authors Gloire Rubambiza, Michael Foster
#@version 03/22/2017

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import tweepy

access_token = "249732925-"+str(sys.argv[1])
access_token_secret = str(sys.argv[2])
consumer_key = str(sys.argv[3])
consumer_secret = str(sys.argv[4])

class TweetListener(StreamListener):

    def on_data(self, data):
        # print(data)
        extract_tweet(data)
        return True
    #End of on_data

    def on_error(self, status):
        print(status)
        exit(2)
    #End of on_error

def extract_tweet(json_str):

    #extracting tweet and user information
    json_dict = json.loads(json_str)
    user_id_str = json_dict['user']['id_str']
    tweet_time = json_dict['created_at'] 
    tweet = json_dict['text'] #extract the tweet
    retweet_status = json_dict['is_quote_status']
    tweet_id_str = json_dict['id_str']
    location = ""
    if(json_dict['user']['geo_enabled'] ):
       location = json_dict['user']['location']
    else:
       location = 'global'

    #all fields below are extracted just in case of future needs
    followers = json_dict['user']['followers_count']
    friends = json_dict['user']['friends_count']
    user_name = json_dict['user']['screen_name']

    #tried extracting full tweet, still getting the keys wrong
    #tweet = json_dict['entities']['extended_text']['full_text']

    tweet_object = {
		    "tweet_id": tweet_id_str,
		    "created_at": tweet_time,
		    "location": location,
                    "tweet": tweet, 
             	    "followers":followers, 
	            "friends": friends,
                    "user_name": user_name,
		     "is_retweet": retweet_status
                    }

    tweet_summary = {
		   "user_id_str" : user_id_str, 
		   "tweet":tweet_object
		   }
    print("\n\n" + str(tweet_summary) + "\n\n")
    batch_file = "April_TB_"+str(sys.argv[5])+"_"+str(sys.argv[6])+".json"
    print("\n About to write to file named %s \n" % batch_file)
    with open(batch_file, 'a') as m:
        json.dump(tweet_summary, m)
        m.write(",\n\n")
    m.close()
#End of extract

if __name__ == '__main__':

    #Open the file containing the ids
    user_ids = []

    with open("follower_screen_names.txt") as f:
       content = f.readlines()
       content = [x.strip() for x in content]

    for item in content:
       # Extract the actual user id and take out noise
       current_user = item.split(',')[0]
       if current_user != "USER UNAVAILABLE" and current_user != "Moreno" and current_user != "verified" and current_user != "6BillionPeople":
          user_ids.append(current_user)
        

    #This handles twitter auth and connection to streaming API
    listener = TweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    #Look into handling time outs and rate limits on the streaming
    stream = Stream(auth, listener)

    # Need to change the offset based on what was passed in by the bash script
    offsetStart = int(sys.argv[5])
    offsetEnd = int(sys.argv[6])
    stream.filter(track=user_ids[offsetStart:offsetEnd])
    
   
    
