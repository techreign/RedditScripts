import sys
import configparser
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
SUBJECT = "Badly Recieved Submission"
MESSAGE = "It seems your post of {} was not taken too well. Try to do a quick Reddit and/or Google search or make " \
          " submission more clear and concise."


def main():
    reddit = praw.Reddit(client_id=ID,
                         client_secret=SECRET,
                         username=USERNAME,
                         password=PASSWORD,
                         user_agent=USER_AGENT)

    print("Authenticated", file=sys.stderr)
    subreddit = reddit.subreddit(SUB_REDDIT).new(limit=10)
    for submission in subreddit:
        print(submission.title + " : " + str(submission.score))
        if submission.score < 0:
            bad_author = submission.author
            if bad_author != reddit.user.me():
                reddit.redditor(bad_author).message(SUBJECT, MESSAGE.format(submission.title))

if __name__ == "__main__":
    main()
