#config.py
import tweepy
import logging

# logging to facilitate debug processes
logger = logging.getLogger()

def creates_twitter_object():
    #creates API object for Twitter Developer account
    consumer_key = "YOUR CONSUMER KEY"
    consumer_secret = "YOUR CONSUMER SECRET"
    access_token = "YOUR ACCESS TOKEN"
    access_token_secret = "YOUR ACCESS TOKEN SECRET"

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
