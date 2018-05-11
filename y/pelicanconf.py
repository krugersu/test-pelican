#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Привалов'
SITENAME = 'Test Pelican'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'Russian'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISQUS_SITENAME = True

# for nice-blog theme
# SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
#

# for Just-Read theme
DISQUS_SITENAME = ''

DEFAULT_DATE_FORMAT = '%d/%m/%Y'
REVERSE_ARCHIVE_ORDER = True
TAG_CLOUD_STEPS = 8

PATH = ''
THEME = ''
OUTPUT_PATH = ''

MARKUP = 'md'


FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

GOOGLE_ANALYTICS = 'UA-XXXXX-X'
HTML_LANG = 'es'
TWITTER_USERNAME = ''

SOCIAL = (('GitHub',  'http://github.com/yourusername'),
          ('Twitter', 'http://twitter.com/yourusername'),)
#####


# THEME = 'D:/home/Project/testpel/src/template/chunk'
# THEME = 'D:/home/Project/testpel/src/template/blueidea'
# THEME = 'D:/home/Project/testpel/src/template/semantic'
# THEME = 'D:/home/Project/testpel/src/template/elegant'
# THEME = 'D:/home/Project/testpel/src/template/foundation'
THEME = 'D:/home/Project/testpel/src/template/Just-Read'  # !
# THEME = 'D:/home/Project/testpel/src/template/lannisport'
# THEME = 'D:/home/Project/testpel/src/template/minimalX' ----------
#THEME = 'D:/home/Project/testpel/src/template/nice-blog' # !
# THEME = 'D:/home/Project/testpel/src/template/nikhil-theme' ------------------
# THEME = 'D:/home/Project/testpel/src/template/pelican-blue'# !
# THEME = 'D:/home/Project/testpel/src/template/plumage'
# THEME = 'D:/home/Project/testpel/src/template/semantic-ui'
# THEME = 'D:/home/Project/testpel/src/template/voce'

















# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

FEED_ALL_RSS = 'rss/all.xml'
CATEGORY_FEED_RSS = 'rss/%s.xml'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
