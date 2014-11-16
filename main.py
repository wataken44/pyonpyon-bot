#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py


"""

import os
import random
import sys

import webapp2


APP_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_ROOT_DIR + '/lib/')

from util.config import load_config
load_config(APP_ROOT_DIR + "/config.json")

random.seed()

application = webapp2.WSGIApplication([
    ('/__task__/fetch', 'handler.fetch_handler.FetchHandler'),
    ('/__task__/post', 'handler.post_handler.PostHandler'),
    ('/__task__/follow', 'handler.follow_handler.FollowHandler'),
    ])
