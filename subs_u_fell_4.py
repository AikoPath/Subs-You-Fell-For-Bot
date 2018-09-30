import praw
import json
from selenium import webdriver

with open('CONFIG', 'r') as f:
    config = json.load(f)

reddit = praw.Reddit(client_id=config['REDDIT']['PERSONAL_USE_SCRIPT'],
                     client_secret=config['REDDIT']['SECRET_KEY'],
                     user_agent=config['REDDIT']['APP_NAME'],
                     username=config['REDDIT']['USER_NAME'],
                     password=config['REDDIT']['PASSWORD'])


def takeScreenshot(comment_permalink):
    driver = webdriver.Chrome('webdriver/chromedriver')
    driver.get('https://reddit.com{}?context=2&depth=3'.format(comment_permalink))
    driver.save_screenshot('my_screenshot.png')
#   TODO driver.get_screenshot_as_png()
    driver.quit()


if __name__ == '__main__':
    for comment in reddit.subreddit('all').stream.comments():
        if comment.body.encode("utf-8").lower() == '/r/subsyoufellfor':
            print('Found one at {}'.format(comment.permalink))
            takeScreenshot(comment.permalink)
