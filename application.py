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

from flask import Flask
import os

app = Flask(__name__)

#{{{ Pages
class pages():
    @app.route('/' methods=['GET'])
    def index():
        return render_template('start.html')
#}}}
