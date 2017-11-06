import os.path
import ruamel.yaml as yaml
from modelbender.metamodel import messages
from modelbender.metamodel import errors

DEBUG=True  # FIXME should come from environment
MSG = messages.Messenger(DEBUG)

def valid_yaml(fname):
    """Returns True if fname is yaml that can be safely parsed."""
    try:
        with open(fname, "r") as infile:
            yaml.safe_load(infile)
        return True
    except:
        MSG.invalid_yaml(fname)
        return False

class Params:
    """A convenient abstraction over the CLI parameters."""
    def __init__(self, kwargs):
        self._kwargs = kwargs
        self._root = '/work/'

    def infile(self):
        return os.path.join(self._root,  self._kwargs['indir'])

    def enterprise_yaml(self):
        return os.path.join(self.infile(), 'enterprise.yaml')


class Config:
    """A convenient abstraction over the YAML configuration (metamodel).

    This provides an aggregated view over the sum of all YAML, after
    tree-walking the pointers in various files.
    """
    def __init__(self, params):
        """ The very boring Config constructor

        This parses the yaml into native python dict, and then does a bunch
        of brain-dead shuffling onto itself, while making some maybe-usefult
        snipes/hints/suggestions about the state of the yaml.

        It doesn't do anything interesting, such as inference or translation.
        """
        self.enterprise = {}
        
        enterprise_yaml_fname = params.enterprise_yaml()
        
        if valid_yaml(enterprise_yaml_fname):
            self._enterprise_yaml_fname = enterprise_yaml_fname
        else:
            raise errors.InvalidEnterpriseYamlError()
        ent_yml = yaml.safe_load(open(enterprise_yaml_fname, "r"))
        if 'name' not in ent_yml.keys():
            raise errors.NamelessEnterpriseYamlError()
        
        self.enterprise['name'] = ent_yml['name']
        self.enterprise['domains'] ={}
        if 'domains' not in ent_yml.keys():
            raise errors.DomainlessEnterpriseError()
        
        my_doms ={}
        for dk in ent_yml['domains'].keys():
            MSG.domain_found(dk)
            fname = os.path.join(params.infile(), ent_yml['domains'][dk])
            MSG.domain_path(fname)
            if not valid_yaml(fname):
                raise errors.InvalidDomainYamlError()
            my_doms[dk] = {}
            dom_yaml = yaml.safe_load(open(fname, 'r'))
            my_doms[dk] = {}
            rsrs_keys = []
            for k in dom_yaml.keys():
                rsrs_keys.append("{}".format(k))
            if 'resources' not in rsrs_keys:
                MSG.domain_without_resources(dk)
            else:
                my_doms[dk]['resources'] = {}
                for resource in dom_yaml['resources'].keys():
                    my_res = {}
                    #
                    # spec
                    if 'spec' in dom_yaml['resources'][resource].keys():
                        spec = dom_yaml['resources'][resource]['spec']
                        my_res['spec'] = spec
                    else:
                        MSG.resource_without_spec(resource)
                    #
                    # canonical
                    if 'canonical' not in dom_yaml['resources'][resource].keys():
                        MSG.resource_without_canonical(dk, resource)
                        my_res['canonical'] = False
                    else:
                        canon =dom_yaml['resources'][resource]['canonical']
                        my_res['canonical'] = canon
                    #
                    # product
                    # <-- TODO
                    
                    # refernces
                    if 'references' not in dom_yaml['resources'][resource].keys():
                        MSG.resource_without_references(dk, resource)
                    else:
                        my_res['references'] = {}
                        references = dom_yaml['resources'][resource]['references']
                        for k in references.keys():
                            my_res['references'][k] = references[k]
                            MSG.resource_has_reference(dk, resource, references[k], k)
                my_doms[dk]['resources'][resource] = my_res
        self.enterprise['domains'][dk] = my_doms

    def list_domains(self):
        found = []
        for k in self.enterprise['domains'].keys():
            found.append(k)
        return found

    def list_resources(self, domain):
        resources = self.enterprise['domains'][domain][domain]['resources']  # WHY oh WHY
        r_keys = []
        for k in resources.keys():
            r_keys.append(k)
        return r_keys

    def get_resource(self, domain, resource):
        if resource not in self.list_resources(domain):
            raise errors.ResourceNotFoundInDomainError()
        doms = self.enterprise['domains']
        return doms[domain]['resources'][resource]
        
    def resource_spec(self, domain, resource):
        rsrc =self.get_resource(domain, resource)
        if 'spec' not in rsrc:
            return None
        return rsrc['spec']

    def resource_canonical(self, domain, resource):
        rsrc =self.get_resource(domain, resource)
        if 'canonical' not in rsrc:
            return None
        return rsrc['canonical']

    def list_resource_references(self, domain, resource):
        rsrc =self.get_resource(domain, resource)
        if 'canonical' not in rsrc:
            return None
        if self.resource_canonical(domain, resource):
            raise errors.CanonicalResourceWithReferentialDependancyError()
        refkeys = []
        for k, v in rsrc['refernces']:
            refkeys.append(k)
        return refkeys
