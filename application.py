#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Gabriel Fornaeus <gf@hax0r.se>
#
# Distributed under terms of the GPLv3 license.

"""
This is an application which compares compare-sites
"""

from wtforms import Form, BooleanField, StringField, validators
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from flask and stuff'
