# followback.py

import tweepy
import logging
from config import creates_twitter_object
import time

#saving log to file
logging.basicConfig(filename='followback.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def follow_back(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Started following {follower.name}")
            follower.follow()

def main():
    api = creates_twitter_object()
    while True:
        follow_back(api)
        logger.info("Sleeping...")
        print('Running')
        time.sleep(60)

if __name__ == "__main__":
    main()
