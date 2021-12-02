#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nathan Esau'
SITENAME = 'Advent of Code 2021 Blog'
SITEURL = '/advent_of_code_2021'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Website', 'https://nathanesau.github.io'),
         ('Github', 'https://github.com/nathanesau'),
         ('Repository', 'https://github.com/nathanesau/advent_of_code_2021'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Flex'
STATIC_PATHS = ['img', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'

DISQUS_SITENAME = 'nathanesau'
GOOGLE_ANALYTICS = "UA-214131892-1"
