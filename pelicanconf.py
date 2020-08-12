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

STATIC_PATHS = ['images', 'extra/CNAME', 'admin', 'podcast']

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'theme'

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'podcast']

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

PODCAST = {
    'title': 'Podcast Músicas para Missa',
    'link': 'https://blog.musicasparamissa.com.br/',
    'language': 'pt-br',
    'description': 'Reflexões sobre a liturgia da palavra e dicas para selecionar músicas litúrgicas para a missa.',
    'itunes': {
        'subtitle': 'Reflexões sobre a liturgia da palavra e dicas para selecionar músicas litúrgicas para a missa.',
        'author': 'Músicas para Missa',
        'summary': 'Reflexões sobre a liturgia da palavra e dicas para selecionar músicas litúrgicas para a missa.',
        'owner': {
            'name': 'Músicas para Missa',
            'email': 'gustavo@musicasparamissa.com.br'
        },
        'image': 'https://blog.musicasparamissa.com.br/images/podcast-icon.jpg',
        'category': 'Religion &amp; Spirituality'
    },
    'item': {
        'linkTemplate': 'https://blog.musicasparamissa.com.br/{0}/',
        'audioTemplate': 'https://blog.musicasparamissa.com.br/podcast/{0}.mp3'
    }
}

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = '{slug}/'
AUTHOR_SAVE_AS = '{slug}/index.html'



AUTHORS = {
    'Gustavo Furtado de Oliveira Alves': {
        'summary':'É mestre em computação aplicada pelo Institudo Nacional de Pesquisas Espaciais, '+
                  'Engenheiro da Computação pela ETEP Faculdades e '+
                  'Técnico em Informática pela Escola Técnica Pandiá Calógeras. '+
                  'Possui as certificações ASF, SCWCD e SCJP e trabalha com desenvolvimento de softwares desde 2007.',
        'image': '/images/foto-gustavo-90x90.jpg'
    },
    'Maikon Máximo': {
        'summary':'Baterista católico profissional. Criador do projeto <b>Porque sou católico</b>. '+
        'Entre em contato e saiba como levar uma Palestra, Formação, Luau e/ou Show com Maikon Máximo para tua cidade, catequese, paróquia, grupo, pastoral... '+
        '<h3>Contato</h3><ul><li>Estado de São Paulo: (11) 98965-0018 Letícia</li><li>Demais regiões: (33) 8447-8524 - Farlei</li></ul>'+
        '<h3>Redes sociais</h3> <ul><li><a href="https://www.facebook.com/maikdrum">Facebook.com/maikdrum</a></li>'+
                  '<li><a href="https://instagram.com/maikonmaximo">Instagram.com/maikonmaximo</a></li>'+
                  '<li><a href="https://youTube.com/maikonmaximo">YouTube.com/maikonmaximo</a></li></ul>',
        'image': '/images/maikon-maximo-90x90.jpg'
    }
}
