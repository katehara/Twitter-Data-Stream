# Twitter-Data-Stream

###Language:
Python3

###Libraries used:
Tweepy
SQLAlchemy(ORM)
pyinotify
threading 
yaml

###Database: 
PostgreSQL 9.5

###Task: 
1. Read configuration from yaml file 
2. Define model to store collected tweets (not all attributes) in postgreSQL DB via SQLAlchemy ORM
3. Stream tweets from Twitter API using tweepy 
4. Watch configuration file for any changes
5. restart stream on modification of configuration with new settings
