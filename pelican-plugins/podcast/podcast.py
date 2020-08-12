# -*- coding: utf-8 -*-
'''
Podcast
-------

The podcast plugin generates plain-text or XML RSS podcasts.
'''

from __future__ import unicode_literals

import re
import collections
import os.path

from datetime import datetime
from logging import warning, info
from codecs import open
from pytz import timezone

from pelican import signals, contents
from pelican.utils import get_date


XML_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
<channel>
<title>{0}</title>
<link>{1}</link>
<language>{2}</language>
<itunes:subtitle>{3}</itunes:subtitle>
<itunes:author>{4}</itunes:author>
<itunes:summary>{5}</itunes:summary>
<description>{6}</description>
<itunes:owner>
    <itunes:name>{7}</itunes:name>
    <itunes:email>{8}</itunes:email>
</itunes:owner>
<itunes:explicit>no</itunes:explicit>
<itunes:image href="{9}" />
<itunes:category text="{10}"/>
"""

XML_ITEM = """
<item>
    <title>{0}</title>
    <description>{1}</description>
    <link>{2}</link>
    <enclosure url="{3}" type="audio/mpeg" length="1024"></enclosure>
    <pubDate>{4}</pubDate>
    <itunes:author>{5}</itunes:author>
    <itunes:duration>{6}</itunes:duration>
    <itunes:explicit>no</itunes:explicit>
    <itunes:image href="{7}"/>
    <itunes:summary>{8}</itunes:summary>
    <guid>{9}</guid>
</item> 
"""

XML_FOOTER = """
</channel>
</rss>
"""


def format_date(date):
    if date.tzinfo:
        tz = date.strftime('%z')
        tz = tz[:-2] + ':' + tz[-2:]
    else:
        tz = "-00:00"
    return date.strftime("%Y-%m-%dT%H:%M:%S") + tz

class PodcastGenerator(object):

    def __init__(self, context, settings, path, theme, output_path, *null):

        self.output_path = output_path
        self.context = context
        self.now = datetime.now()
        self.siteurl = settings.get('SITEURL')


        self.default_timezone = settings.get('TIMEZONE', 'UTC')
        self.timezone = getattr(self, 'timezone', self.default_timezone)
        self.timezone = timezone(self.timezone)

        config = settings.get('PODCAST', {})

        if not isinstance(config, dict):
            warning("podcast plugin: the PODCAST setting must be a dict")
        else:
            self.config = config

    def write_item(self, article, fd):

        if not hasattr(article, 'tags'):
            return
            
        
        if not 'Podcast' in getattr(article, 'tags'):
            return

        if getattr(article, 'status', 'published') != 'published':
            return
           
        if getattr(article, 'private', 'False') == 'True':
            return

        # We can disable categories/authors/etc by using False instead of ''
        if not article.save_as:
            return

        page_path = os.path.join(self.output_path, article.save_as)
        if not os.path.exists(page_path):
            return

        #Exclude URLs from the sitemap:
        fd.write(XML_ITEM.format(
            article.title, 
            article.description, 
            self.config['item']['linkTemplate'].format(article.slug),
            self.config['item']['audioTemplate'].format(article.slug),
            article.date,
            article.author,
            article.duration,
            article.image,
            article.description,
            self.config['item']['linkTemplate'].format(article.slug)
        ))

    def generate_output(self, writer):
        path = os.path.join(self.output_path, 'podcast.xml')

        info('writing {0}'.format(path))

        with open(path, 'w', encoding='utf-8') as fd:

            fd.write(XML_HEADER.format(
                self.config['title'], 
                self.config['link'],
                self.config['language'],
                self.config['itunes']['subtitle'],
                self.config['itunes']['author'],
                self.config['itunes']['summary'],
                self.config['description'],
                self.config['itunes']['owner']['name'],
                self.config['itunes']['owner']['email'],
                self.config['itunes']['image'],
                self.config['itunes']['category']))

            for article in self.context['articles']:
                self.write_item(article, fd)

            fd.write(XML_FOOTER)


def get_generators(generators):
    return PodcastGenerator


def register():
    signals.get_generators.connect(get_generators)
