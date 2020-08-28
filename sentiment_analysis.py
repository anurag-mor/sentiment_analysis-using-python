import tweepy
from textblob import TextBlob

consumer_key = 'xxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxx'

access_token = 'xxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxx'

auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

tweets = api.search('politics')

for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
