# retweeter.py
import tweepy
import logging
from config import creates_twitter_object
import time

#saving log to file
logging.basicConfig(level=logging.INFO, filename='retweeter.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def main():
    api = creates_twitter_object()
    #the usernames of the account you wanna get tweets
    screen_names = ["realpython", "geeksforgeeks","dsc_ubuea", "djangoproject", "ThePSF"]
    logger.info("Fetching tweets all tweets")
    for screen_name in screen_names:
    	logger.info(f"Fetching tweets of {screen_name}")
    	print("Fetching tweets of "+ screen_name)
    	#count = 2, looks only for the latest 2 tweets for each user
    	statuses = api.user_timeline(screen_name, count = 2)
    	for status in statuses:
    		if status.in_reply_to_status_id is not None:
    			# if tweet is a reply continue
    			continue
    		if not status.favorited:
    		          # Like the the tweet
    		          try:
    		          	status.favorite()
    		          except Exception as e:
    		          	logger.error(f"Error while liking tweet with id {status.id}", exc_info=True)
    		if not status.retweeted:
    		      #Retweet, since we have not retweeted it yet
    		      try:
    		      	api.retweet(status.id)
    		      except Exception as e:
    		      	logger.error(f"Error while retweeting tweet with id {status.id}", exc_info=True)


if __name__ == "__main__":
    main()
