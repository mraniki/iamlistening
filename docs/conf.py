# Configuration file for the Sphinx documentation builder.

import os
import sys
from os.path import abspath, dirname

import sphinx_bootstrap_theme

sys.path.insert(0, os.path.abspath('../'))
path = dirname(abspath(__file__))
sys.path.append(path)

# -- Project information -----------------------------------------------------

project = 'iamlistening'
copyright = '2023, mraniki'
author = 'mraniki'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx', 
    'sphinx.ext.viewcode',  
    'sphinx_autodoc_typehints', 
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxext.remoteliteralinclude',
    'sphinx_togglebutton',
    'notfound.extension'
]

intersphinx_mapping = {
    "talky": ("http://talkytrader.github.io/wiki/", None),
}

# -- Extension configuration ---------------------------------------------------

napoleon_google_docstring = True
autosummary_generate = True
autoclass_content = 'both'
html_show_sourcelink = True
autodoc_inherit_docstrings = True 
set_type_checking_flag = True 
autodoc_member_order = 'bysource'
add_module_names = True


master_doc = 'index'
source_suffix = ['.rst', '.md']
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
html_logo = '_static/favicon.png'
html_favicon = '_static/favicon.ico'

html_theme_options = {

    'source_link_position': "footer",
    'bootswatch_theme': "darkly",
    'bootstrap_version': "3",
    'globaltoc_depth': 2,
    'globaltoc_includehidden': "true",
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'navbar_site_name': "TT",
    'navbar_links': [
        ("Talky", "https://talkytrader.github.io/wiki/",True),
        ("IamListening",  "_iamlistening_index"),
        ("_menu",  "Plugins",[
            ("IamListening",  "_iamlistening_index", True ),
        ]),
        ("Github", "https://github.com/mraniki/tt", True),
    ]

}


def setup(app):
    app.add_css_file("custom.css")

