import os
import json
from pymongo import MongoClient


def readData(file):
	with open(os.path.join(path,file) , 'r') as f: data = f.read()
	tweets = json.loads('['+data+']')
	return tweets

def removeDuplicates(tweets, ids, filteredTweets)
	for i in tweets:
		if i['id'] not in ids:
			ids += [i['id']]
			filteredTweets += [i]

def toMongoDB(tweets):
	# with open('final.json', 'r') as file: data = json.load(file)
	# start a mongodb instance from command line - 'mongod' or 'sudo service mongod [start/stop/restart]'
	client = MongoClient('mongodb://localhost:27017/') # connect to mongod server
	tweetdb = client.demon_india # create new db named 'demon_india' (demon - demonetisation)
	alltweets = tweetdb.all_tweets # tweets + retweets collected from twitter Search API via tweepy (See ../toJson for more details)
	originaltweets = tweetdb.tweets # filter out retweets and extract tweets from them
	users = tweetdb.users # users collection

	allids = []
	origids = []
	userids = []
	for tw in data['tweets']:
		# store all tweets 
		if tw['id'] not in allids:
			allids += [tw['id']]
			all_tweets.insert(tw)
		#store users
		if tw['user']['id'] not in userids:
			userids += [tw['user']['id']]
			users.insert(tw['user'])
		#check if it a retweet
		if 'retweeted_status' in tw : 
			tw = tw['retweeted_status']
			#store user of original tweet too
			if tw['user']['id'] not in userids:
				userids += [tw['user']['id']]
				users.insert(tw['user'])
		# store only original tweets 
		if tw['id'] not in origids:
			origids += [tw['id']]
			originaltweets.insert(tw)



if __name__ == '__main__':

	path = os.getcwd()+'/datafiles' # folder containing all the collected tweet files
	ids = []
	filteredTweets = []
	for filename in os.listdir(path):
		tweets = readData(filename)
		removeDuplicates(tweets, ids, filteredTweets)
	print(len(ids))
	toMongoDB(filteredTweets)
	#with open('final.json', 'w') as outfile: json.dump({"tweets" : filteredTweets}, outfile)
