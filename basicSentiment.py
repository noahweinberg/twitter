import tweepy as tp
from textblob import TextBlob

cons_key = ''
cons_secret = ''

a_token = ''
a_token_secret = ''

auth = tp.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(a_token, a_token_secret)

api = tp.API(auth)

public_tweets = api.search('Coronavirus')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


	
