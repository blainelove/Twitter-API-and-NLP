# Using Tweepy to interact with Twitter API to search Twiter on any term and conduct natural language processing sentiment analysis 

# Prompt for user input and then utilize reusable function which inputs a search term and outputs to the user:
# 1) each tweet
# 2) the average subjectivity of the results
# 3) the average polarity of the results

import tweepy
from textblob import TextBlob 
import TwitterTokens #importing my Twitter passwords from a seperate file that I did not want to publish to GitHub

#storing my Twitter tokens
access_token = TwitterTokens.access_token 
access_token_secret = TwitterTokens.access_token_secret
consumer_key = TwitterTokens.consumer_key
consumer_secret = TwitterTokens.consumer_secret

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


def searchTwitter(term):
	""" Search for Tweets with the given term and outputs the average polarity and subjectivity of the tweets. """
	subjectivity = 0 #initiating counter variables 
	polarity = 0
	count = 0
	public_tweets = api.search(term)
	for tweet in public_tweets:
		print(tweet.text)
		count += 1
		analysis = TextBlob(tweet.text)
		subjectivity += analysis.sentiment.subjectivity 
		polarity += analysis.sentiment.polarity
	print("\n")
	print("Average subjectivity is " + str(subjectivity/count)) #dividing subjectivity and polarity by count to print average
	print("Average polarity is " + str(polarity/count))

#Get user input for the term to search on Twitter
searchTerm = input("Enter term to search: ")
searchTwitter(searchTerm)