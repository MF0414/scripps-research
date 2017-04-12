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

print("sys arg0" ,sys.argv[0])
print("sys arg1 ", sys.argv[1])
access_token = "249732925-"+str(sys.argv[1])
print(access_token)
access_token_secret = str(sys.argv[2])
print(access_token_secret)
consumer_key = str(sys.argv[3])
print("%s %s" % (sys.argv[5], sys.argv[6]))
#print("Token %s, token secret %s, consumer_key %s" + 
      #"offset %d, offsetend %d" % (access_token, access_token_secret, consumer_key, int(sys.argv[5]), int(sys.argv[6])))
consumer_secret = str(sys.argv[4])
print(consumer_secret)

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
    with open('ModMarchTweets.json', 'a') as m:
        json.dump(tweet_summary, m)
#End of extract

if __name__ == '__main__':

    #Open the file containing the ids
    user_ids = []

    with open("follower_screen_names.txt") as f:
       content = f.readlines()
       content = [x.strip() for x in content]

    for item in content:
        # Extract the actual user id
        #print(item.split(',')[0])
        user_ids.append(item.split(',')[0])

    #This handles twitter auth and connection to streaming API
    listener = TweetListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    #Look into handling time outs and rate limits on the streaming
    stream = Stream(auth, listener)


    #Filter to listen for the first GVSU followers
    #api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)
    #u = api.get_user(screen_name = 'GloireKnowsBest')
    #myID = str(u.id)
    # Need to change the offset based on what was passed in by the bash script
    offsetStart = int(sys.argv[5])
    offsetEnd = int(sys.argv[6])
    print(offsetStart)
    print(offsetEnd)
    
    #for user in range (offsetStart,offsetEnd):
        #print("Processing this user %s" % user_ids[user])
    #stream.filter(track=user_ids[offsetStart:offsetEnd])
    
   
    
