# -*- coding: utf-8 -*-
#
# Dash documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 29 11:17:04 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Dash'
copyright = u'2024, Dash Core Group, Inc'
author = u'strophy,thephez'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'latest'
# The full version, including alpha/beta/rc tags.
release = u'latest'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = None

locale_dirs = ['locale/']
gettext_compact = False 

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'README.md',
    '.devcontainer',
    'transifex',
    'docs/user/wallets/electrum/dip3_p2sh_howto.md'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'none'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------



# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'hoverxref.extension',
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_search.extension',
    'sphinx.ext.intersphinx',
]

hoverxref_role_types = {
    'hoverxref': 'tooltip',
}

# -- Myst parser configuration -----------------------------------------------
# Auto-generate header anchors for md headings
myst_heading_anchors = 5

# Enable colon_fence for better markdown compatibility
# https://myst.tools/docs/mystjs/syntax-overview#directives
myst_enable_extensions = ["colon_fence"]

# -- intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    "core": ("https://docs.dash.org/projects/core/en/stable/", None),
    "platform": ("https://docs.dash.org/projects/platform/en/stable/", None),
}

# We recommend adding the following config value.
# Sphinx defaults to automatically resolve *unresolved* labels using all your Intersphinx mappings.
# This behavior has unintended side-effects, namely that documentations local references can
# suddenly resolve to an external location.
# See also:
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes
intersphinx_disabled_reftypes = ["*"]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "external_links": [
        {"name": "Core docs", "url": "https://docs.dash.org/projects/core/en/stable/docs/index.html"},
        {"name": "Platform docs", "url": "https://docs.dash.org/projects/platform/en/stable/docs/index.html"},
        {"name": "Dash.org", "url": "https://www.dash.org"},
        {"name": "Forum", "url": "https://www.dash.org/forum"},
    ],
    "use_edit_page_button": True,
    "github_url": "https://github.com/dashpay/docs",
    "show_toc_level": 2,
    "show_nav_level": 1,
    "favicons": [
      {
         "rel": "icon",
         "sizes": "16x16",
         "href": "img/favicon-16x16.png",
      },
      {
         "rel": "icon",
         "sizes": "32x32",
         "href": "img/favicon-32x32.png",
      },
      {
         "rel": "icon",
         "sizes": "96x96",
         "href": "img/favicon-96x96.png",
      },
      {
         "rel": "icon",
         "sizes": "144x144",
         "href": "img/favicon-144x144.png",
      },
   ],
   "footer_start": ["copyright"],
   "footer_center": ["sphinx-version"],
   "footer_end": ["theme-version"],      
#    "navbar_start": ["navbar-logo", "languages"],
#    "navbar_center": ["languages", "navbar-nav", "languages"],
#    "navbar_end": ["navbar-icon-links", "version"],
#    "secondary_sidebar_items": ["languages", "page-toc", "edit-this-page", "sourcelink"],
#    "footer_items": ["languages", "copyright", "sphinx-version", "theme-version"],
   "primary_sidebar_end": ["languages"],
}

html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "dashpay",
    "github_repo": "docs",
    "github_version": "20.0.0",
    "doc_path": "",
}

html_logo = 'docs/user/img/dash_logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/footer.css',
    'css/pydata-overrides.css',
]

# Override to allow text wrap in tables
# Details: https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
#html_context = {
#    'css_files': [
#        '_static/theme_overrides.css',  # override wide tables in RTD theme
#        ],
#     }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
html_sidebars = {
    "index": ["sidebar-main.html"],
    "**": ["sidebar-nav-bs"]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Dashdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Dash.tex', u'Dash Documentation',
     u'strophy', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dash', u'Dash Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Dash', u'Dash Documentation',
     author, 'Dash', 'A revolutionary digital money system, Dash is Digital Cash',
     'Miscellaneous'),
]

def setup(app):
    app.add_js_file('js/lang.js')
    app.add_js_file('js/pydata-search-close.js')
