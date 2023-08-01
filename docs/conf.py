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
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxext.remoteliteralinclude',
    'sphinx_togglebutton',
    'notfound.extension'
]


# -- Napoleon Settings ------

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True

autosummary_generate = True
autoclass_content = 'both'
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
# html_logo = '_static/favicon.png'
# html_favicon = '_static/favicon.ico'

html_theme_options = {
    'source_link_position': "footer",
    'bootswatch_theme': "darkly",
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'globaltoc_depth': -1,
    'bootstrap_version': "3",
    'navbar_links': [("Install", "01_install"),
                     ("Module", "02_module"),
                     ("Settings", "03_settings"),
                     ("Github", "https://github.com/mraniki/iamlistening", True),
                     ("Talky", "https://talkytrader.github.io/wiki/", True),
                     ],
                     }


def setup(app):
    app.add_css_file("custom.css")

