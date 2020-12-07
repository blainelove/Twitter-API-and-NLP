#Using Tweepy to interact with Twitter API to update status

import tweepy
import TwitterTokens #importing my Twitter passwords from a seperate file that I did not want to publish to GitHub

access_token = TwitterTokens.access_token #storing my twitter tokens into variables 
access_token_secret = TwitterTokens.access_token_secret
consumer_key = TwitterTokens.consumer_key
consumer_secret = TwitterTokens.consumer_secret

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

def tweetText(message):
    """ Update Twitter status with text only. """
    if message:
        try:
            api.update_status(status=message)
            return "Status update successful!"
        except Exception as e:
            return "Something went wrong! Got exception: {}".format(e)      
    return "Please enter a message."

def tweetMedia(img, message):
    """ Update Twitter status with media and text. """
    if img and message:
        try:
            api.update_with_media(img, status=message)
            return "Status update with media successful!"
        except Exception as e:
            return "Something went wrong! Got exception: {}".format(e)
    return "Please give an image and message."

#Usage
print(tweetText("Hello World!!!"))
print(tweetMedia("pug.jpg", "I love pugs!<3"))


