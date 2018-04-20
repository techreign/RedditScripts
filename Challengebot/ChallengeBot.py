import sys
import configparser
import math
import time
import praw

# read credentials from login file
config = configparser.ConfigParser()
config.read('my.ini')

# login info
ID = config.get('Authentication', 'Client_id')
SECRET = config.get('Authentication', 'Client_secret')
USERNAME = config.get('Authentication', 'Username')
PASSWORD = config.get('Authentication', 'Password')
USER_AGENT = config.get('Authentication', 'User_agent')

SUB_REDDIT = config.get('Authentication', 'Sub_reddit')
SUBJECT = "New challenge!"
MESSAGE = " New Challenge: 100 pushups for 30 days "
INTERVAL = 100      # set the interval to how often you want this bot to post


def main():
    reddit = praw.Reddit(client_id=ID,
                         client_secret=SECRET,
                         username=USERNAME,
                         password=PASSWORD,
                         user_agent=USER_AGENT)
    print("Authenticated", file=sys.stderr)

    start = time.time()
    while True:
        end = time.time()
        time_elapsed = math.ceil(-1 * (start - end))
        print(time_elapsed)
        if time_elapsed == interval:
            reddit.subreddit(SUB_REDDIT).submit(SUBJECT, selftext=MESSAGE)
            start = time.time()
            print("posted new submission")


if __name__ == "__main__":
    main()
