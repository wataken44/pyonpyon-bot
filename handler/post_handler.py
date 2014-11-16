#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" post_handler.py


"""

from handler.twitter_base_handler import TwitterBaseHandler
from model.file_model import FileModel

class PostHandler(TwitterBaseHandler):
    def get(self):
        history = FileModel.read("history")
        if history is None:
            return

        time = history[0][0]
        count = history[0][1]
        text = u"ご注文はうさぎですか？　第1羽は %d 回再生されてます。 http://nico.ms/1397552685 #so23335421 #nicoch" % count

        self._twitter.update_status(text)
