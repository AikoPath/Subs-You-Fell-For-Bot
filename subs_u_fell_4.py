import praw
import json

with open('CONFIG', 'r') as f:
    config = json.load(f)

reddit = praw.Reddit(client_id=config['REDDIT']['PERSONAL_USE_SCRIPT'],
                     client_secret=config['REDDIT']['SECRET_KEY'],
                     user_agent=config['REDDIT']['APP_NAME'],
                     username=config['REDDIT']['USER_NAME'],
                     password=config['REDDIT']['PASSWORD'])


if __name__ == '__main__':
    for comment in reddit.subreddit('all').stream.comments():
        if comment.body.encode("utf-8").lower() == '/r/subsyoufellfor':
            print(comment)
