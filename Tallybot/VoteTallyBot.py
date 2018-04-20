import praw
import sys
import configparser

# read credentials from login file
config = configparser.ConfigParser()
config.read('my.ini')

# login info
ID = config.get('Authentication', 'Client_id')
SECRET = config.get('Authentication', 'Client_secret')
USER_AGENT = config.get('Authentication', 'User_agent')

POLL_NAME = config.get('Poll', 'Poll_name')
POLL_ITEMS_STRING = config.get('Poll', 'Poll_items')
POLL_ITEMS_LIST = POLL_ITEMS_STRING.split(",")
NUM_POLL_ITEMS = len(POLL_ITEMS_LIST)
MY_URL = config.get('Poll', 'my_url')


def main():
    # setting a reddit object without logging in
    reddit = praw.Reddit(client_id=ID,
                         client_secret=SECRET,
                         user_agent=USER_AGENT)

    submission_to_query = reddit.submission(url=MY_URL)

    counter_list = make_counter_list(NUM_POLL_ITEMS)

    print("Reddit accessed", file=sys.stderr)
    search_in(submission_to_query, counter_list)
    write_to_file(POLL_ITEMS_LIST, counter_list)


def make_counter_list(size):
    counter_list = []
    for i in range(0, size):
        counter_list.append(0)
    return counter_list


def search_in(submission, counter_list):
    comments = submission.comments.list()
    print("Submission found", file=sys.stderr)
    if len(comments) > 0:
        for comment in comments:
            for i in range(0, NUM_POLL_ITEMS):
                if POLL_ITEMS_LIST[i] in comment.body:
                    counter_list[i] += 1
    print("Finished tallying the poll", file=sys.stderr)


def write_to_file(poll_items, poll_counts):
    f = open('results.txt', 'w')
    for i in range(0, NUM_POLL_ITEMS):
        f.write(poll_items[i] + ": " + str(poll_counts[i]) + "\n")
    print("Finish writing results to results.txt file", file=sys.stderr)
    f.close()

if __name__ == "__main__":
    main()
