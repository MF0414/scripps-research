import tweepy

access_token = "1666122888-uSWuz7YnSKiLmnBZ0ccglCColQJzufxaMhAPSU4"
access_token_secret = "37eLiYE2Zv1KJ386ZSHWZhXSyTpqtyfDKAtzxcklnJjui"
consumer_key = "cekJqEoqofOPKs3R5jVegGNlJ"
consumer_secret = "MRSHPhwEf30Y9pKkwIE7eYMuPk3bK6UqaaFCvVR5V8PBVeDvC6"


from pymongo import MongoClient
client = MongoClient()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)


def get_friends(user_id):
    users = []
    page_count = 0
    for user in tweepy.Cursor(api.friends, id=user_id, count=200).pages():
        page_count += 1
        print 'Getting page {} for friends'.format(page_count)
        users.extend(user)
    return users

def get_followers_ids(user_id):
    ids = []
    page_count = 0
    for page in tweepy.Cursor(api.followers_ids, id=user_id, count=5000).pages():
        page_count += 1
        print 'Getting page {} for followers ids'.format(page_count)
        ids.extend(page)

    return ids

def get_friends_ids(user_id):
    ids = []
    page_count = 0
    for page in tweepy.Cursor(api.friends_ids, sc=user_id, count=5000).pages():
        page_count += 1
        print 'Getting page {} for friends ids'.format(page_count)
        ids.extend(page)
    return ids

def process_user(user):
    user_id = 'GVSU'

    follower_ids = get_followers_ids(user['screen_name'])
    friend_ids = get_friends_ids(user['screen_name'])


if __name__ == "__main__":

    process_user('GVSU')
