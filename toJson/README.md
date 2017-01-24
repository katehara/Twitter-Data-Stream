## Twitter-Data-Stream-to-JSON-File

###Language:
Python3

###Libraries used:
Tweepy<br>
yaml<br>
json<br>

###Task: 
1. Read configuration from yaml file 
2. Search tweets from Twitter Search API using tweepy 
3. Store in file as JSON objects to avoid losing any details and properties of tweets

####Note:
Files collected using this script are stored at location : ../toMongo/datafiles/<br>
1. cashless*.json are collected using keyword 'cashless india' 
2. demonitisation*.json are collected using keyword 'demonitisation' 
3. digitalIndia*.json are collected using keyword 'digital india' 

These files may contain duplicate entries due to various factors which will be filtered while storing them into MongoDB