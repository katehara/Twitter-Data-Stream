import tweepy
import json
import time
import yaml

with open('config.yaml') as file: conf = yaml.load(file)
settings = conf['settings']
consumer_key = settings['ck']
consumer_secret = settings['cs']
access_token = settings['at']
access_token_secret = settings['ats']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchquery = "demonetisation"

users =tweepy.Cursor(api.search,q=searchquery).items()
count = 0
errorCount=0

file = open('demon.json', 'w') 

while True:
    try:
        user = next(users)
        count += 1
    except tweepy.TweepError:
        print ("sleeping....")
        time.sleep(60*16)
        user = next(users)
    except StopIteration:
        break
    try:
        print ("Writing to JSON tweet number:"+str(count))
        json.dump(user._json,file,sort_keys = True,indent = 4)
        
    except UnicodeEncodeError:
        errorCount += 1
        print ("UnicodeEncodeError,errorCount ="+str(errorCount))

print ("completed, errorCount ="+str(errorCount)+" total tweets="+str(count))
    