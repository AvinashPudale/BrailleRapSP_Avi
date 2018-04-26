# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
import sys

import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")



sys.path.append(os.path.abspath('_ext'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    
]
templates_path = ['_templates']

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'index'
project = u'BrailleRap-SP'
copyright = '2018-{}, BrailleRap-SP Team'

version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'

#intersphinx_mapping = {
#    'python': ('http://python.readthedocs.io/en/latest/', None),
#    'django': ('http://django.readthedocs.io/en/1.8.x/', None),
#    'sphinx': ('http://sphinx.readthedocs.io/en/latest/', None),
#}
htmlhelp_basename = 'BrailleRapSPdoc'
latex_documents = [
    ('index', 'ReadTheDocs.tex', u'Read the Docs Documentation',
     u'Eric Holscher, Charlie Leifer, Bobby Grace', 'manual'),
]

#man_pages = [
#    ('index', 'read-the-docs', u'Read the Docs Documentation',
#     [u'Eric Holscher, Charlie Leifer, Bobby Grace'], 1)
#]

exclude_patterns = [
    # 'api' # needed for ``make gettext`` to not die.
]

language = 'fr'

#locale_dirs = [
#    'locale/',
#]
gettext_compact = False

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_theme_path = ["_themes"]
#html_logo = 'img/logo.svg'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
}


def setup(app):
    app.add_stylesheet('custom.css')