import tweepy
from textblob import TextBlob

consumer_key = 'aRd3XW2UZsDX5nr6uKrp74Oij'
consumer_secret = 'WScCnVpVTYNjdS0PXc651spbAkf010NbOKcvSCU1qNZvUoouSH'

access_token = '365552981-9u9SnZ5wZGkHvJHgyKaL3IQ7wHFpO4gfwDeDkk8p'
access_token_secret = 'YZXdJsVF6CrJodoZNG8YkHDj9PsRnZAP5hdAUKZaZu8iA'

auth_handler = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

tweets = api.search('politics')

for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)