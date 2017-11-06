ENTERPRISE = "{} Enterprise".format("{{ ctx }}")

AUTHOR="TODO"
extensions = ['sphinx.ext.viewcode',
              'sphinx.ext.graphviz',
              'sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Model Bender'
copyright = '2017, {}'.format(AUTHOR)
author = AUTHOR
version = '0.0'
release = '0.0'
language = None
exclude_patterns = ['_build', 'Thumbs.db',
                    '.DS_Store', '.venv']
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
htmlhelp_basename = '{{ ctx }}'
latex_elements = {
    'papersize': 'a4paper',
}
latex_toplevel_sectioning="part"
latex_documents = [
    (master_doc, '{{ ctx }}.tex', '{{ ctx }}',
     AUTHOR, 'manual'),
]
texinfo_documents = [
    (master_doc, '{{ CTX }}', '{{ CTX }} Documentation',
     author, '{{ CTX }}',
     'Enterprise integration surface model for {{ CTX }}',
     'Miscellaneous'),
]
