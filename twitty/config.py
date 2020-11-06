#config.py
import tweepy
import logging
from user import *

# logging to facilitate debug processes
logger = logging.getLogger()

def creates_twitter_object():
    #creates API object for Twitter Developer account
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    # check if credentials are valid
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
