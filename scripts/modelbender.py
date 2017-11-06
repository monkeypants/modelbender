import os.path
import os
import click
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from modelbender.metamodel.enterprise import Enterprise, Domain
from modelbender.metamodel import messages
from modelbender.metamodel import errors
from modelbender import config

INDIR_HELP = "the directory containing the metamodel yaml"
OUTDIR_HELP = "the directory wher you want your generated docs" 

#
# CLI stuff
#
@click.group()
@click.version_option(version='0.0.0')
def main():
    """Over-arching hook for the click CLI program."""
    pass

@main.command()
@click.option("--indir", default="metamodel", help=INDIR_HELP)
@click.option("--outdir", default="_tmp", help=OUTDIR_HELP)
def enterprise(**kwargs):
    """Create the top-level enterprise document"""
    pass

@main.command()
@click.option("--domain")
@click.option("--indir", default="metamodel", help=INDIR_HELP)
@click.option("--outdir", default="_tmp", help=OUTDIR_HELP)
def domain(**kwargs):
    """Create detailed domain documentation"""
    pass

@main.command()
@click.option("--indir", default="metamodel", help=INDIR_HELP)
def validate(**kwargs):
    """Check the metmodel for yaml errors"""
    prms = config.Params(kwargs)
    e_yml = prms.enterprise_yaml()
    if config.valid_yaml(e_yml):
        print("{} is valid yaml".format(e_yml))
    else:
        print("{} is NOT valid yaml, aborting".format(e_yml))
        exit
    # pass go, collect $200
    enterprise = load_metamodel(prms)

    
def load_metamodel(params):
    """Levers the metamodel out of yaml and into python.

    This is important because for all subsequent behavior, we want first-class
    python objects with convenience methods for e.g. for template rendering.
    """
    cfg = config.Config(params)
    
    e = Enterprise(cfg.enterprise['name'])
    for domain in cfg.list_domains():
        for resource in cfg.list_resources(domain):
            print("DEBUG: json parsed OK for {}.{}".format(domain, resource))
            #canonical = resource_canonical(domain, product, resource)
            #spec = resource_spec(domain, product, resource)
            #refernces = resource_refernces(domain, product, resource)
            #if references:
            #    for k, v in refernces:
            #        print("{}.{}.{}.{}: {}".format(domain, product, resource, k, v))
            # create resource
            # with spec, canonical and references
    return e


if __name__ == '__main__':
    # bend the model
    main()
