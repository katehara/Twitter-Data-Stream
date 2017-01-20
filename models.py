from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text, create_engine, inspect
import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  
Session = sessionmaker()
class Tweets(Base):
	__tablename__ = 'tweets'
	id = Column(Numeric, primary_key=True)	
	created_at = Column(DateTime)
	user_screen_name = Column(String(70))
	user_followers_count = Column(Integer)
	retweet_count = Column(Integer)
	favorite_count = Column(Integer)
	text = Column(String(200))
	user_id =  Column(Numeric)
	user_listed_count = Column(Integer)
	user_statuses_count = Column(Integer)
	user_friends_count = Column(Integer)
	user_favourites_count = Column(Integer)
	new_cat = Column(String(50))

	def __init__(self,id ,created_at,user_screen_name,user_followers_count,retweet_count,favorite_count,text,
				 user_id,user_listed_count,user_statuses_count,user_friends_count,user_favourites_count,new_cat):
		self.id = id
		self.created_at = created_at
		self.user_screen_name = user_screen_name
		self.user_followers_count = user_followers_count 
		self.retweet_count = retweet_count
		self.favorite_count = favorite_count
		self.text = text
		self.user_id = user_id
		self.user_listed_count = user_listed_count
		self.user_statuses_count = user_statuses_count
		self.user_friends_count = user_friends_count
		self.user_favourites_count = user_favourites_count

def checkDB(connection_string):
	if not (database_exists(connection_string)):
		create_database(connection_string)

def checkTB(connection_string):
	db = sqlalchemy.create_engine(connection_string)  
	global engine
	engine = db.connect()  
	meta = sqlalchemy.MetaData(engine)
	Session.configure(bind=engine)
	Base.metadata.create_all(engine,checkfirst=True)    
	global session
	session = Session()

def connect(dbs):
	connection_string = 'postgresql://'+dbs['user']+':'+dbs['pswd']+'@'+dbs['host']+':'+dbs['port']+'/'+dbs['database']
	checkDB(connection_string)
	checkTB(connection_string)

def disconnect():
	session.close()

def insert(tweet):
	new_cat = categorize((tweet.text).lower())
	newT = Tweets(tweet.id, 
		tweet.created_at, 
		tweet.user.screen_name, 
		tweet.user.followers_count ,
		tweet.retweet_count,
		tweet.favorite_count,
		tweet.text,
		tweet.user.id,
		tweet.user.listed_count,
		tweet.user.statuses_count,
		tweet.user.friends_count,
		tweet.user.favourites_count)
	print('writing tweet : ' + tweet.id + ' by ' + tweet.user.screen_name)
	# Upsert operation of SQLAlchemy
	merged = session.merge(newT)
	session.commit()
	return
