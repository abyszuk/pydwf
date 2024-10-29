# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

extradirs = ['.', '../../source']

sys.path = [os.path.abspath(path) for path in extradirs] + sys.path

# -- Project information -----------------------------------------------------

project = 'pydwf'
copyright = '2019–2023, Sidney Cadot'
author = 'Sidney Cadot'

# The full version, including alpha/beta/rc tags
release = '1.1.17'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx.ext.graphviz"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Autodoc options


# autodoc has the absurd behavior to consider the signature of an __init__ method as the signature
# of a class (what a concept), and render it after the class name in the documentation.
#
# This is extremely confusing; if anything, people would expect the base class(es) there, not
# the __init__ signature.
#
# This should work to fix it, but it doesn't:
#
#     autodoc_class_signature = 'separate'
#
# A workaround for now is to add "()" at the end of all autoclass directives.

autodoc_default_options = {
    'members': True,
    'member-order' : 'bysource'
    #'special-members' : '__init__',
    #'inherited-members': True,
    #'undoc-members': True,
    #'exclude-members': '__weakref__'
}

# Omit type package prefixes as much as possible.
add_module_names = False
python_use_unqualified_type_names = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_logo = "logo/pydwf-logo-200x125.png"

html_theme_options = {
    'style_nav_header_background': '#73a886'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "custom.css"
]

# -- Options for LaTeX output -------------------------------------------------

latex_elements = {
    'papersize' : 'a4paper',
    'preamble'  : '\setcounter{tocdepth}{999}'
}

latex_toplevel_sectioning = 'chapter'

latex_logo="logo/pydwf-logo.pdf"

todo_include_todos = True

intersphinx_mapping = {
    "python"     : ('https://docs.python.org/3/', None),
    "numpy"      : ('https://numpy.org/doc/stable/', None),
    "matplotlib" : ('https://matplotlib.org/stable/', None)
}
