import os.path
import os
import stat
import click
import sys
import inspect
from jinja2 import Environment, PackageLoader, select_autoescape

# what is this rubbish!
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from modelbender.metamodel.enterprise import Enterprise
from modelbender.metamodel.domain import Domain
from modelbender.metamodel.service import CanonicalService, AuthorativeService
from modelbender.metamodel import messages
from modelbender.metamodel import errors
from modelbender import config

jenv = Environment(
    loader=PackageLoader('modelbender', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

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
    prms = config.Params(kwargs)
    enterprise = load_metamodel(prms)
    outdir = prms.outdir()

    rst_template = jenv.get_template('index.rst')
    md_template = jenv.get_template('index.md')
    makefile_template = jenv.get_template('Makefile')
    confpy_template = jenv.get_template('conf.py')
    requirements_template = jenv.get_template('requirements.txt')
    gitignore_template = jenv.get_template('.gitignore')
    venvsh_template = jenv.get_template('venv.sh')
    readme_template = jenv.get_template('README.txt')
    todo_template = jenv.get_template('TODO.txt')

    base_fname = os.path.join('/work', outdir)
    rst_fname = os.path.join(base_fname, "index.rst")
    md_fname = os.path.join(base_fname, "index.md")
    makefile_fname = os.path.join(base_fname, "Makefile")
    confpy_fname = os.path.join(base_fname, "conf.py")
    requirements_fname = os.path.join(base_fname, "requirements.txt")
    gitignore_fname = os.path.join(base_fname, ".gitignore")
    venvsh_fname = os.path.join(base_fname, "venv.sh")
    readme_fname = os.path.join(base_fname, "README.txt")
    todo_fname = os.path.join(base_fname, "TODO.txt")
    root_files = (
        (rst_template, rst_fname),
        (md_template, md_fname),
        (makefile_template, makefile_fname),
        (confpy_template, confpy_fname),
        (requirements_template, requirements_fname),
        (gitignore_template, gitignore_fname),
        (venvsh_template, venvsh_fname),
        (readme_template, readme_fname),
        (todo_template, todo_fname)
    )
    for template, fname in root_files:
        os.makedirs(os.path.dirname(fname), exist_ok=True)
        fp = open(fname, 'w')
        fp.write(template.render(ctx=enterprise))
        fp.close()
        print("generating {}".format(fname))

    # kludge: venv.sh needs to be executable
    st = os.stat(venvsh_fname)
    os.chmod(venvsh_fname, st.st_mode | stat.S_IEXEC)  # bitwise-or

    # now descend into domains...
    for d in enterprise.get_domains():
       generate_domain(enterprise, d, outdir)



@main.command()
@click.option("--domain")
@click.option("--indir", default="metamodel", help=INDIR_HELP)
@click.option("--outdir", default="_tmp", help=OUTDIR_HELP)
def domain(**kwargs):
    """Create detailed domain documentation"""
    prms = config.Params(kwargs)
    enterprise = load_metamodel(prms)
    domain_name = prms.domain()
    if not enterprise.has_domain_named(domain_name):
        raise Exception(
            "domain '{}' not in enterprise '{}'".format(
                domain_name, enterprise))
    else:
        my_domain = enterprise.get_domain_named(domain_name)
    my_indir = prms.indir()
    my_outdir = prms.outdir()
    generate_domain(enterprise, my_domain, my_outdir)


def generate_domain(enterprise, domain_name, outdir):
    if not enterprise.has_domain_named(domain_name):
        raise Exception(
            "domain '{}' not in enterprise '{}'".format(
                domain_name, enterprise))
    else:
        my_domain = enterprise.get_domain_named(domain_name)

    base_fname = os.path.join('/work', outdir, 'domains')
    domain_dir =os.path.join(base_fname, str(my_domain)) # FIXME: make safe filename string of domain
    
    # generate resource-level docs
    for my_resource in my_domain.get_resources():    
        resource_files = (
            (
                jenv.get_template('resource_statechart_block.diag'),
                os.path.join(domain_dir, "{}_statechart_block.diag".format(str(my_resource)))
            ),
            (
                jenv.get_template('resource.rst'),
                os.path.join(domain_dir, "{}.rst".format(str(my_resource)))  
            )
        )    
        for template, fname in resource_files:
            os.makedirs(os.path.dirname(fname), exist_ok=True)
            fp = open(fname, 'w')
            fp.write(template.render(resource=my_resource))
            fp.close()
            print("generating {}".format(fname))


    
    # generate service-level docs
    '''
    services = []
    for my_resource in my_domain.get_resources():
        pass
        service = my_resource.get_service()
        if service not in services:
            services.append(service)
    for service in services:
        # FIXME: resolve resource/service confusion in codebase
        # TODO: simplify, loop over my_domain.get_services()
        pass
    '''
    
    # generate domain-level docs
    base_fname = os.path.join('/work', outdir, 'domains')
    domain_files = (
        (
            jenv.get_template('domain.rst'),
            os.path.join(base_fname, "{}.rst".format(str(my_domain)))
        ),
    )    
    for template, fname in domain_files:
        os.makedirs(os.path.dirname(fname), exist_ok=True)
        fp = open(fname, 'w')
        fp.write(template.render(domain=my_domain))
        fp.close()
        print("generating {}".format(fname))

    #for s in my_domain.get_services():
    #    generate_service(enterprise, my_domain, str(s), outdir)

    
    
'''
@main.command()
@click.option("--domain")
@click.option("--service")
@click.option("--indir", default="metamodel", help=INDIR_HELP)
@click.option("--outdir", default="_tmp", help=OUTDIR_HELP)
def service(**kwargs):
    """Create detailed documentation for service in a domain"""
    prms = config.Params(kwargs)
    enterprise = load_metamodel(prms)
    domain_name = prms.domain()
    service_name = prms.service()
    outdir = prms.outdir()
    generate_service(enterprise, domain_name, service_name, outdir)
'''
'''
def generate_service(enterprise, domain_name, service_name, outdir):
    if not enterprise.has_domain_named(domain_name):
        raise Exception(
            "domain '{}' not in enterprise '{}'".format(
                domain_name, enterprise))
    else:
        my_domain = enterprise.get_domain_named(domain_name)
    if not my_domain.has_service_named(service_name):
        raise Exception(
            "service '{}.{}' not in enterprise '{}'".format(
                domain_name, service_name, enterprise))
    else:
        my_service = my_domain.get_service_named(service_name)

    rst_template = jenv.get_template('service.rst')
    erd_template = jenv.get_template('service_erd.dot')
    statechart_template = jenv.get_template('service_statechart.dot')

    base_fname = os.path.join('/work', outdir, 'domains', str(my_domain))
    rst_fname = os.path.join(base_fname, "{}.rst".format(str(my_service)))
    erd_fname = os.path.join(base_fname, "{}_erd.dot".format(str(my_service)))
    statechart_fname = os.path.join(base_fname, "{}_statechart.dot".format(str(my_service)))

    for template, fname in (
            (rst_template, rst_fname),
            (erd_template, erd_fname),
            (statechart_template, statechart_fname)):
        os.makedirs(os.path.dirname(fname), exist_ok=True)
        fp = open(fname, 'w')
        fp.write(template.render(service=my_service))
        fp.close()
        print("generating {}".format(fname))
'''

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
    # walk the config tree (yaml) and populate
    # the enterprise with domains and services
    for dom in cfg.list_domains():
        d = Domain(e, dom)
        #TODO: fix the config tree s/resource/service/g
        for service in cfg.list_resources(dom):
            tl = []
            transitions = cfg.resource_transitions(dom, service)
            if transitions:
                for transition in transitions:
                    if "from_state" in transition.keys():
                        from_state = transition["from_state"]
                    else:
                        from_state = None
                    if "to_state" in transition.keys():
                        to_state = transition["to_state"]
                    else:
                        to_state = None
                    if "name" in transition.keys():
                        name = transition["name"]
                    else:
                        name = None
                    tl.append({'from_state':from_state,
                               'to_state':to_state,
                               'name':name})
            else:
                raise Exception("{} transitions: {}.{}".format(transitions, dom, service))
            # canonical, authorative or referential
            if cfg.resource_is_canonical(dom, service):
                s = CanonicalService(service, d, tl)
            elif cfg.resource_is_authorative(dom, service):
                s = AuthorativeService(service, d, tl)
            else:
                s = ReferentialService(service, d, tl)
            # FIXME: process primary and secondary IDs
            #s.primary_id = cfg.primary_id_of_service(dom, service)
            d.add_service(s)
        e.add_domain(d)
    # Walk the enterprise and populate
    # the service details from config.
    # This requires two passes because otherwise
    # we can't validate that parents exist (etc).
    for dom in e.get_domains():
        for service in dom.get_services():    
            # process parents
            parents = cfg.parents_of_service(str(dom), str(service))
            if parents:
                for p in parents:
                    service.add_parent_named(p)
                    # the bug is that we are looking into _services before
                    # we have finished adding them

            # process services consumed
            # TODO: move to language of "external references"
            consumed = cfg.services_consumed(dom, service)
            if consumed:
                for c_attribute in consumed.keys():
                    c_value = consumed[c_attribute]
                    (c_domain, c_resource, c_identifier) = c_value.split(".")
                    service.add_reference(c_domain, c_resource, c_identifier)

            # FIXME: process swagger specs
            # FIXME: process statecharts
    return e


if __name__ == '__main__':
    # bend the model
    main()
