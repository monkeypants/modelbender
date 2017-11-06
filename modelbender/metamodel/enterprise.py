from modelbender.metamodel.domain import Domain

class Enterprise:
    """
    An enterprise is a named system, composed from the services
    that are provided by a collection of domains.

    The Enterprise class exists in the meta model to be the root
    node in an object tree that is the enterprise model. This single
    enterprise instance is used to collect and manage the Domains
    in the enterprise model.
    """
    def __init__(self, name):
        self.name = name
        self._domains = []

    def get_domains(self):
        return self._domains

    def num_domains(self):
        return len(self.get_domains())

    def add_domain(self, domain):
        if not isinstance(domain, Domain):
            tmpl = "{} is not a {}"
            msg = tmpl.format(domain, Domain)
            raise Exception(msg)
        if domain not in self._domains:
            self._domains.append(domain)

    def __str__(self):
        return self.name


