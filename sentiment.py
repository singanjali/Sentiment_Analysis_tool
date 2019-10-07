#realtime sentiment analisys of tweets

import re
import tweepy
import matplotlib.pyplot as plt
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
def __init__(self):

consumer_key = '7yJ2TNPrJNQ6YzXFELwCnvZ0L'
consumer_secret = 'lEO3M2efbCTPsNT3URRjz7qWvty5UylXN3r9LPxPmJEOmLCPXv'
access_token = '3152691702-j5DjdwrtfCItfJtieTfhuXzQZJzo9Eepx9d9pGv'
access_token_secret = 'y6TiZtxPUb5IY88f8lhYedsAMkcCADIW3XYNiQZa9vg4j'

try:
self.auth = OAuthHandler(consumer_key, consumer_secret)

self.auth.set_access_token(access_token, access_token_secret)

self.api = tweepy.API(self.auth)
except:
print("Error: Authentication Failed")

def clean_tweet(self, tweet):

return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(self, tweet):

analysis = TextBlob(self.clean_tweet(tweet))

if analysis.sentiment.polarity > 0:
return 'positive'
elif analysis.sentiment.polarity == 0:
return 'neutral'
else:
return 'negative'

def get_tweets(self, query, count):

tweets = []

try:

fetched_tweets = self.api.search(q = query, count = count)

for tweet in fetched_tweets:

parsed_tweet = {}


parsed_tweet['text'] = tweet.text

parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

if tweet.retweet_count > 0:

if parsed_tweet not in tweets:
tweets.append(parsed_tweet)
else:
tweets.append(parsed_tweet)

return tweets

except tweepy.TweepError as e:
print("Error : " + str(e))

def main():

api = TwitterClient()

val = input("write the movie name you want the review ")
tweets = api.get_tweets(query = val, count = 200)

ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
pos=100*len(ptweets)/len(tweets)
print("Positive tweets percentage: {} %".format(pos))

ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
neg = 100 * len(ntweets) / len(tweets)
print("Negative tweets percentage: {} %".format(neg))

neu=len(tweets) - len(ntweets) - len(ptweets)
Neu = 100*neu/len(tweets)
print("Neutral tweets percentage: {} %".format(Neu))

x_axix = ["positive", "negative", "neutral"]
y_axis = [pos , neg ,Neu]
plt.plot(x_axix , y_axis)
plt.show()



print("\n\nPositive tweets:")
for tweet in ptweets[:10]:
print(tweet['text'])


print("\n\nNegative tweets:")
for tweet in ntweets[:10]:
print(tweet['text'])

if __name__ == "__main__":

main()
