## Twitter-Data-Stream-to-JSON-File

###Language:
Python3

###Libraries used:
PyMongo<br>
os<br>
json<br>

###Task: 
1. Read all files containing stored tweets (from toJson) 
2. Organize them into mongoDB collections 

####Note:
There are three collections: <br>
1. all_tweets (89004) : All collected tweets <br>
2. tweets (30475) : contains original tweets (not retweets). Original tweets have been taken from 'retweeted_status' property of retweets<br>
3. users (42307) : all users of tweets and retweets <br>
