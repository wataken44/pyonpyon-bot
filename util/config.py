#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" config.py


"""

import json

config = {}

def load_config(path):
    global config
    fp = open(path)
    config = json.load(fp)
    fp.close()

def get_config():
    global config
    return config
