#Simple extraction class and its important user attributes
#@authors Gloire Rubambiza, Michael Foster
#@version 03/08/2017

import json

class tweetextract(object):
    
    def __init__(self, data):
        data = data
    #Fin du constructor
    

    def extract_tweet(self, json_dict):

        #extracting tweet and user information
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
        followers = json_dicst['user']['followers_count']
        friends = json_dicst['user']['friends_count']
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

        with open('ModMarchTweets.json', 'a') as m:
            json.dump(tweet_summary, m)
    #Fin d'ExtracTweet
