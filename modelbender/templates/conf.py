import os

COPYRIGHT = os.environ.get("DOCUMENT_COPYRIGHT", "(not speficied)")
AUTHOR = os.environ.get("DOCUMENT_AUTHOR", "(not speficied)")
VERSION = "TODO"  # TODO: use the git short-hash, with '-dirty' appended if local changes
RELEASE = VERSION  # TODO: use version unless some environment variable set?

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
    'sphinxcontrib.actdiag',
    'sphinxcontrib.nwdiag',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = '{{ ctx }}'
copyright = COPYRIGHT
author = AUTHOR
version = VERSION
release = RELEASE
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
    '**': ['about.html', 'navigation.html', 'searchbox.html']
}

htmlhelp_basename = '{{ ctx }}doc'  # TODO: lower, strip spaces
latex_elements = {
    'papersize': 'a4paper',
}
latex_documents = [
    (master_doc, '{}.tex'.format(htmlhelp_basename), u'{{ ctx }} Documentation',
     AUTHOR, 'manual'),
]
man_pages = [
    (master_doc, '{{ ctx }}',  # TODO: lower, strip spaces
     u'{{ ctx }} Documentation', [author], 1)
]
texinfo_documents = [
    (master_doc, '{{ ctx }}',  # TODO: lower, strip spaces
     u'{{ ctx }} core Documentation',
     author, '{{ ctx }}',  # TODO: lower, strip spaces
     'One line description of project.',
     'Miscellaneous'),
]
