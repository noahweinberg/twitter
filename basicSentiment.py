import tweepy as tp
from textblob import TextBlob

cons_key = 'yvTVlnvwHw2MPCWIo2TkYR75k'
cons_secret = 'c3WUqknCWbiaxwpIELfhyfOEBfMM3iFEBm0sw3nro7TdeBkFmN'

a_token = '1205694345325809664-6cpxodbVxPSwlFc6DVxwvrjutRS5qE'
a_token_secret = 'sdhU3kLTeojBdEN4I9pr8LDQplYKqPgfQ69Jb41bPlDGw'

auth = tp.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(a_token, a_token_secret)

api = tp.API(auth)

public_tweets = api.search('Coronavirus')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


	
