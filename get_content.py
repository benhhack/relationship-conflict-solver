'''
Gets pictures from Twitter page dog_rates
'''
import tweepy
from tweepy import OAuthHandler
import json
import os

consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_TOKEN_SECRET')


@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profile
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='dog_rates',
                           count=200, include_rts=False,
                           exclude_replies=True)

last_id = tweets[-1].id

while (True):
    more_tweets = api.user_timeline(screen_name='dog_rates',
                                    count=200,
                                    include_rts=False,
                                    exclude_replies=True,
                                    max_id=last_id - 1)
    # There are no more tweets
    if (len(more_tweets) == 0):
        break
    else:
        last_id = more_tweets[-1].id - 1
        tweets = tweets + more_tweets

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])
