from paver.easy import *
import paver.doctools
#from paver import setuputils
from paver.setuputils import setup
#from distutils.core import setup

#options(
#    setup=dict(
setup(
    name='modebender',
    version='0.1.0',
    description='Tool for generating useful views of a simply modelled enterprise',
    author='Chris Gough',
    author_email='christopher.d.gough+modelbender@gmail.com',
    url='https://github.com/monkeypants/modelbender',
    packages=['modelbender', 'modelbender.metamodel'],
    package_data=paver.setuputils.find_package_data(
        "modelbender",
        package="modelbender",
        only_in_packages=False
    ),
    install_requires=[],
    test_suite='nose.collector',
    zip_safe=False,
    entry_points="""
    [console_scripts]
    modelbender = paver.command:main
    """,
)

options(
    sphinx=Bunch(
        builddir="_build",
        sourcedir="."
    )
)

@task
@needs('paver.doctools.html')
def html():
    """Build Modelbender's documentation and install it into modelbender/docs"""
    builtdocs = path("docs") / options.sphinx.builddir / "html"
    destdir = path("modelbender") / "docs"
    destdir.rmtree()
    builtdocs.move(destdir)
