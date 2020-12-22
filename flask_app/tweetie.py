"""
Reference:
* https://github.com/parrt/msds692/blob/master/hw/code/sentiment/tweetie.py
"""
from numpy.lib.npyio import load
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from numpy import median


def loadkeys(filename):
    """ "
    load twitter api keys/tokens from CSV file with form
    consumer_key, consumer_secret, access_token, access_token_secret
    """
    with open(filename) as f:
        items = f.readline().strip().split(", ")
        return items


def authenticate(twitter_auth_filename):
    """
    Given a file name containing the Twitter keys and tokens,
    create and return a tweepy API object.

    Args:
        twitter_auth_filename (str): path to the twitter auth file

    Returns:
        (tweepy.api)
    """
    consumer_key, consumer_secret, access_token, access_token_secret = loadkeys(
        twitter_auth_filename
    )
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def fetch_tweets(api, name):
    """
    Given a tweepy API object and the screen name of the Twitter user,
    create a list of tweets where each tweet is a dictionary with the
    following keys:
       id: tweet ID
       created: tweet creation date
       retweeted: number of retweets
       text: text of the tweet
       hashtags: list of hashtags mentioned in the tweet
       urls: list of URLs mentioned in the tweet
       mentions: list of screen names mentioned in the tweet
       score: the "compound" polarity score from vader's polarity_scores()
    Return a dictionary containing keys-value pairs:
       user: user's screen name
       count: number of tweets
       tweets: list of tweets, each tweet is a dictionary
    For efficiency, create a single Vader SentimentIntensityAnalyzer()
    per call to this function, not per tweet.
    """
    vader = SentimentIntensityAnalyzer()
    status_obj = api.user_timeline(screen_name=name, count=100)
    res = {
        "user": name,
        "count": len(status_obj),
        "tweets": [],
        "median_score": 0,
        "mean_score": 0,
    }
    scores = []
    for stat in status_obj:
        tweet = dict()
        tweet["id"] = stat.id_str
        tweet["created"] = stat.created_at
        tweet["retweeted"] = stat.retweeted
        tweet["text"] = stat.text
        tweet["hashtags"] = [hashtag["text"] for hashtag in stat.entities["hashtags"]]
        tweet["urls"] = [url["url"] for url in stat.entities["urls"]]
        tweet["mentions"] = [
            mention["screen_name"] for mention in stat.entities["user_mentions"]
        ]
        tweet["score"] = vader.polarity_scores(stat.text)["compound"]
        res["tweets"].append(tweet)
        scores.append(tweet["score"])
    res["median_score"] = f"{median(scores): .4f}"
    res["mean_score"] = f"{sum(scores) / len(scores): .4f}"
    return res
