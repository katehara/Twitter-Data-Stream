import os
import json
import yaml
import tweepy
from pymongo import MongoClient

with open('config.yaml') as file: conf = yaml.load(file)
settings = conf['settings']
consumer_key = settings['ck']
consumer_secret = settings['cs']
access_token = settings['at']
access_token_secret = settings['ats']

def apiTwitter():
	# authorize tweepy instance using twitter tokens and return api reference
	print('connecting to stream...')
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth, wait_on_rate_limit=True,parser=tweepy.parsers.JSONParser())

def collect():
	print('writing data ... ')
	count = 7000 #where to start data fetching
	client = MongoClient('mongodb://localhost:27017/') # connect to mongod server
	tweetdb = client.demon_india # get the db named 'demon_india' (demon - demonetisation)
	users = tweetdb.users # get users collection from db
	user_info = tweetdb.user_info # create the collection for all user information
	cursor = users.find({}) #get all documents from users collection
	api = apiTwitter() #authorise twitter api
	for u in cursor[count:count+1000]:
		count += 1
		try:		
			handle = u['screen_name']
			item = {
				"user_screen_name" : handle, #unique identifier for each user object
				"user_profile": u, # user profile
				"user_tweets": api.user_timeline(screen_name=handle) #get last 20 tweets for the user
			}	
			user_info.insert(item) #insert in collection user_info
		except Exception:
			pass
		print(count)
	client.close()

collect()