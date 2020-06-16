import praw
import datetime

from auth import CLIENT_ID, CLIENT_SECRET, PASSWORD, USERNAME

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     password=PASSWORD, username=USERNAME,
                     user_agent='script to wish users happy cake day')

for comment in reddit.subreddit('all').stream.comments():
    today_utc = datetime.datetime.now()
    cake_day_utc = datetime.datetime.fromtimestamp(comment.author.created_utc)

    if today_utc.day == cake_day_utc.day and today_utc.month == cake_day_utc.month and cake_day_utc.year != today_utc.year:

        try:
            comment.reply('Happy Cake Day!')

        except praw.exceptions.APIException as e:
            print(e.message)
            pass
