#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" twitter_base_handler.py


"""

import webapp2

import tweepy

from util.config import get_config

class TwitterBaseHandler(webapp2.RequestHandler):
    """ Twitter handler base class

    """

    def __init__(self, *args, **kwargs):
        webapp2.RequestHandler.__init__(self, *args, **kwargs)
        
        twitter_config = get_config()["twitter"]
        
        consumer_key = twitter_config["consumer_key"]
        consumer_secret = twitter_config["consumer_secret"]
        access_token = twitter_config["access_token"]
        access_token_secret = twitter_config["access_token_secret"]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self._twitter = tweepy.API(auth)
        
