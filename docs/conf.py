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
    'navbar_title': "Demo",
    'navbar_site_name': "Site",
    'navbar_pagenav_name': "Page",
    'globaltoc_depth': 2,
    'globaltoc_includehidden': "true",
    'navbar_class': "navbar",
    'navbar_fixed_top': "true",
    'source_link_position': "nav",
    'bootswatch_theme': "sandstone",
    'bootstrap_version': "3",


    # 'navbar_sidebarrel': False,
    # 'navbar_pagenav': False,
    # 'navbar_links': [
    #     ("TalkyTrader", "https://talkytrader.github.io/wiki/",True),
    #     ("_menu",  "Plugins",[
    #         ("IamListening",  "index"),
    #         ("Install",  "IAL_01_install"),
    #         ("_divider", ),
    #     ]),
    #     ("Github", "https://github.com/mraniki/tt", True),
    # ]

}

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]
# html_css_files = [
#     "custom.css",
# ]
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}

# html_logo = '_static/logo-full.png'
html_favicon = '_static/favicon.ico'
# html_copy_source = False
# html_show_sourcelink = False

# def setup(app):
#     app.add_css_file("custom.css")

