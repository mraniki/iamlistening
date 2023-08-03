# Configuration file for the Sphinx documentation builder.

import os
import sys

# from os.path import abspath, dirname
import sphinx_bootstrap_theme

sys.path.insert(0, os.path.abspath('../'))
# path = dirname(abspath(__file__))
# sys.path.append(path)

# -- Project information -----------------------------------------------------

project = 'iamlistening'
copyright = '2023, mraniki'
author = 'mraniki'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',  
    'sphinxext.remoteliteralinclude',
]

# intersphinx_mapping = {
#     "talky": ("http://talkytrader.github.io/wiki/", None),
# }

# -- Extension configuration ---------------------------------------------------

napoleon_google_docstring = True
autosummary_generate = True
autoclass_content = 'both'
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


html_theme_options = {
    'navbar_title': " ",
    'navbar_site_name': "IamListening",
    'navbar_sidebarrel': False,
    'navbar_pagenav_name': "Sections",
    'navbar_pagenav': False,
    'globaltoc_depth': 4,
    'globaltoc_includehidden': "true",
    'navbar_class': "navbar",
    'navbar_fixed_top': "true",
    'source_link_position': "none",

    'bootswatch_theme': "darkly",
    'bootstrap_version': "3",

    'navbar_links': [
        ("TalkyTrader", "https://talkytrader.github.io/wiki/",True),
        ("_menu",  "Plugins",[
            ("IamListening",  "index"),
            ("Install",  "01_setup"),
            ("_divider", ),
        ]),
        ("&#1F419", "https://github.com/mraniki/tt", True),
    ]

}

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]
html_sidebars = {'sidebar': ['globaltoc.html']}

html_logo = '_static/favicon.png'
html_favicon = '_static/favicon.ico'
# html_copy_source = False
# html_show_sourcelink = False

def setup(app):
    app.add_css_file("custom.css")

