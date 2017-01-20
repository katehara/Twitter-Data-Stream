import yaml
import os
import tweepy
import models

class StreamListener(tweepy.StreamListener):
	"""
	This function is a callback for Stream Listener
	"""

	def on_status(self, status):
		# if a tweet is a retweet, take the original tweet and insert into the database
		if hasattr(status , 'retweeted_status'):
			original = status.retweeted_status
		else:
			original = status
		models.insert(original)
		
	def on_error(self, status_code):
		# Don't stop the stream on error in data or api rate limit 
		return True

def readConfig():
	# read configuration for database, twitter tracking keyworkds, and api access tokens
	print('configuring...')
	with open('config.yaml') as file: data = yaml.load(file)
	return data

def connectDB(dbs):
	#connect to the database via models
	print('setting up DB...')
	models.connect(dbs)
	return

def apiTwitter(settings):
	# authorize tweepy instance using twitter tokens and return api reference
	print('connecting to stream...')
	consumer_key = settings['ck']
	consumer_secret = settings['cs']
	access_token = settings['at']
	access_token_secret = settings['ats']
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth, wait_on_rate_limit=True)

def start():
	# string all of the actions together and start streaming
	global conf
	conf = readConfig()
	stream = conf['stream']
	db = conf['db']
	settings = conf['settings']
	connectDB(db)
	global api
	api = apiTwitter(settings)
	keys = stream['handle'] + stream['hashtag']
	print('streaming for : ' + ', '.join(keys))
	stream_listener = StreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
	stream.filter(track=keys)

def disconnect():
	# disconnect from database of stream is stopeed or needs to be restarted
	print('disconnecting DB...')
	models.disconnect()

# if __name__ == '__main__' :
# 	start()
