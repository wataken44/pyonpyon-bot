#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" file_model.py


"""

import pickle
from google.appengine.ext import db

class FileModel(db.Model):
    text = db.BlobProperty()

    @classmethod
    def build_key(cls, name):
        return "file-%s" % name

    @classmethod
    def get_by_name(cls, name):
        return cls.get(cls.build_key(name))

    @classmethod
    def read(cls, name):
        key = cls.build_key(name)
        model = cls.get_or_insert(key, text=pickle.dumps(None))
        return pickle.loads(model.text)

    @classmethod
    def write(cls, name, content):
        key = cls.build_key(name)
        model = cls(key_name=key, text=pickle.dumps(content))
        model.put()
