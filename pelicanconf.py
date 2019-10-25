#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Remy Torro'
SITENAME = 'Of physics and thoughts'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['latex','pelican-cite',"render_math",'better_figures_and_images','pelican_jsmath']
THEME = "/home/remy13127/pelican-themes/html5-dopetrope"
LINKS = (('Photorro','http://photorro.wordpress.com'),)

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
MATH_JAX = {'align':'center','linebreak_automatic':True,'responsive':True}
RESPONSIVE_IMAGES = True
ABOUT_TEXT = 'This website is a collection of notes from my various courses as a student in Physics at Aix-Marseille university.'
ABOUT_IMAGE = 'https://photorro.files.wordpress.com/2018/08/p1440336-01.jpeg?w=700&h='
LINKEDIN_USER = 'rémy-torro-607a50112/en'
MAIL = "remy13127@gmail.com"
RESEARCH_USER = "Remy_Torro"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
