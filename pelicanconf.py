#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gustavo Furtado de Oliveira Alves'
SITENAME = 'Blog Músicas para Missa'
#SITEURL = 'http://localhost:8000'

PATH = 'content'

STATIC_ENDPOINT = 'https://static.musicasparamissa.com.br'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'theme'

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'



AUTHORS = {
    'Gustavo Furtado de Oliveira Alves': {
        'summary':'É mestre em computação aplicada pelo Institudo Nacional de Pesquisas Espaciais, '+
                  'Engenheiro da Computação pela ETEP Faculdades e '+
                  'Técnico em Informática pela Escola Técnica Pandiá Calógeras. '+
                  'Possui as certificações ASF, SCWCD e SCJP e trabalha com desenvolvimento de softwares desde 2007.',
        'image': 'http://gustavofurtado.com.br/images/profile.jpg'
    },
    'Maikon Máximo': {
        'summary':'Baterista profissional. Criador do projeto <b>Porque sou católico</b>. '+
        'Entre em contato e saiba como levar uma Palestra, Formação, Luau e/ou Show com Maikon Máximo para tua cidade, catequese, paróquia, grupo, pastoral... '+
        'Estado de São Paulo: (11) 98965-0018 - Letícia Demais regiões: (33) 8447-8524 - Farlei',
        'image': '/images/maikon-maximo.jpg'
    }
}
