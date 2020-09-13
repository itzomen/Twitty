# retweeter.py
import tweepy
import logging
from config import creates_twitter_object
import time

#saving log to file
logging.basicConfig(level=logging.INFO, filename='retweeter.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
