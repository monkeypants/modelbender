# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
extensions = ['sphinx.ext.viewcode',
              'sphinx.ext.graphviz',
              'sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Model Bender'
copyright = '2017, Chris Gough'
author = 'Chris Gough'
version = '0.0'
release = '0.0'
language = None
exclude_patterns = ['_build', 'Thumbs.db',
                    '.DS_Store', '.venv', '.venv2.7']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
# html_theme_options = {}
html_static_path = ['_static']
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}
htmlhelp_basename = 'ModelBender'
latex_elements = {
    'papersize': 'a2paper',
}
latex_documents = [
    (master_doc, 'model_bender.tex', 'Model Bender',
     'Chris Gough', 'manual'),
]
texinfo_documents = [
    (master_doc, 'ModelBender', 'Model Bender Documentation',
     author, 'ModelBender',
     'MetaModelling framework for opinionated API surface modelling',
     'Miscellaneous'),
]
