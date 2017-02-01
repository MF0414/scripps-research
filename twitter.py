
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"

class StdOutListener(StreamListener):

	def on_data(self, data):
		print(data)
		return True

	def on_error(self, status):
		print(status)

if __name__ == '__main__':

	#This handles twitter auth and connection to streaming API
	listener = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, listener)

	#filer
	stream.filter(track=['trump', 'mfgvsu414']) #, follow=)

