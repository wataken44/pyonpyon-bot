#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" follow_handler.py


"""

import logging
import random

from handler.twitter_base_handler import TwitterBaseHandler

class FollowHandler(TwitterBaseHandler):
    def __init__(self, *args, **kwargs):
        TwitterBaseHandler.__init__(self, *args, **kwargs)
        
    def head(self):
        pass

    def get(self):
        # follower
        cursors = (-1, -1)
        followers_ids = []
        
        for k in range(100):
            ids, cursors = self._twitter.followers_ids(cursor=cursors[1])
            followers_ids += ids
            logging.debug(ids)
            if cursors[1] == 0:
                break
            time.sleep(1) # wait
        followers_set = set(followers_ids)

        
        # following
        cursors = (-1, -1)
        friends_ids = []

        for k in range(100):
            ids, cursors = self._twitter.friends_ids(cursor=cursors[1])
            friends_ids += ids
            logging.debug(ids)            
            if cursors[1] == 0:
                break
            time.sleep(1) # wait
        friends_set = set(friends_ids)

        # follow randomly who newly follow me
        new_follow_ids = followers_set.difference(friends_set)
        prob = len(new_follow_ids) / 8.0
        if random.random() < prob:
            user_id = random.choice(new_follow_ids)
            self._twitter.create_friendship(user_id=user_id, follow=False)
            
        # unfollow randomly who newly unfollow me
        new_unfollow_ids = friends_set.difference(followers_set)
        prob = len(new_unfollow_ids) / 16.0
        if random.random() < prob:
            user_id = random.choice(new_unfollow_ids)
            self._twitter.destroy_friendship(user_id=user_id)
        
