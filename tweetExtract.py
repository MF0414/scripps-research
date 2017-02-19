#Simple extraction of the tweet and its associated user object
import json

data_file = open('OneTweet.txt') #opening the file
json_str = data_file.read() #read the file into a single string

# able to handle one json object but
# throws an "Extra data" valueError when
# attempting to load more than one object
json_dicts = json.loads(json_str) 
#print (type(json_dicts))

user_name = json_dicts['user']['screen_name'] #extract the screen_name
tweet_time = json_dicts['created_at'] #extract the date
followers = json_dicts['user']['followers_count'] #extract the user's followers
friends = json_dicts['user']['friends_count']
tweet = json_dicts['text'] #extract the tweet

#tried extracting full tweet, still getting the keys wrong
#tweet = json_dicts['retweeted_status']['extended_text']['full_text']

tweet_object = {
                "full_tweet":tweet, 
		"followers":followers, 
		"friends": friends
}
tweet_summary = {
		"screen_name": user_name, 
		"tweet":tweet_object
		}

#user_tweets[user_name] = tweet
#print (user_tweets)
print(tweet_summary)


