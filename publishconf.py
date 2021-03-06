#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.musicasparamissa.com.br'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'podcast']

# Following items are often useful when publishing

#DISQUS_SITENAME = ""

MINIFY = {
 'remove_comments': True,
 'remove_all_empty_space': True,
 'remove_optional_attribute_quotes': False
}
