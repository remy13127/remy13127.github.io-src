#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Remy Torro'
SITENAME = 'Of physics and thoughts'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['latex','pelican-cite','render_math','better_figures_and_images']
THEME = "/home/remy13127/pelican-themes/html5-dopetrope"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
PUBLICATIONS_SRC = 'content/zotero.bib'
MATH_JAX = {'linebreak_automatic':True,'responsive':True}
RESPONSIVE_IMAGES = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
