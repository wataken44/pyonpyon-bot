#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" fetch_handler.py


"""

import datetime
import logging
import re

import webapp2
from google.appengine.api import urlfetch

from bs4 import BeautifulSoup

from model.file_model import FileModel

URL = "http://ch.nicovideo.jp/gochiusa/video?sort=f&order=a"
HISTORY_SIZE = 100

class FetchHandler(webapp2.RequestHandler):
    def get(self):
        result = self._fetch()

        if result.status_code != 200:
            logging.error("cannot fetch(%d)" % result.status_code)
            return

        count = self._parse(result.content)

        if count is None:
            logging.error("cannot parse")
            return

        self._save(count)
        
    def _fetch(self):
        global URL
        return urlfetch.fetch(url=URL)
        
    def _parse(self, content):
        soup = BeautifulSoup(content)
        views = soup.findAll("li",{"class": "view"})

        ptn = re.compile('<var>(.*)</var>')
        mo = re.search(ptn, str(views[0]))

        if mo is None:
            return None

        return int(mo.group(1).replace(",",""))

    def _save(self, count):
        global HISTORY_SIZE

        history = FileModel.read("history")
        if history is None:
            history = []

        now = datetime.datetime.utcnow()
        history.insert(0, [now, count])
        history = history[:HISTORY_SIZE]

        FileModel.write("history", history)
