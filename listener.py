# Listens for tweets from GVSU followers
#@authors Gloire Rubambiza
#@version 03/22/2017

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"

class StdOutListener(StreamListener):


    def on_data(self, data):
        """
        Reports if there is any new data
        """
        write(data)
        return True
    #End of on_data

	def on_error(self, status):
        """
        Reports any error encountering during streaming
        """
        print(status)
    #End of on_error

    def write(self, data):
        """
        Writes streaming data to a local file
        Not sure about threading errors yet
        """
        with open('MarchTweets.json', 'w') as m:
            json.dump(data,m)
    #End of write

if __name__ == '__main__':

	#Open the file containing the ids
	user_ids = []

    with open("follower_ids.txt") as f:
       content = f.readlines()
    content = [x.strip() for x in content]

    for item in content:
        # Extract the actual user id
        user_ids.append(item.split(',')[0])

	#This handles twitter auth and connection to streaming API
	listener = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, listener)

	#Filter to listen for the first GVSU followers
	stream.filter(track= user_ids[:1000]) #, follow=)
