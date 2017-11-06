#
# An enterprise is modeled as a collection of domains
#
class Domain:
    """
    A domain:
     * is a collection of distinct Resources.
     * is the semantic authority of at least one concept
     * provides services related to their semantic authority

    The purpose of the Domain class in the meta model is to
    collect and manage resources to the model.
    """
    def __init__(self, enterprise, label):
        enterprise.add_domain(self)
        self.enterprise = enterprise
        self.label = label
        self._resources = []

    def get_enterprise(self):
        return self.enterprise

    def num_resources(self):
        return len(self._resources)

    def get_canonical_resources(self):
        out = []
        for r in self._resources:
            if r.get_type().name == "Canonical":
                out.append(r)
        return out

    def num_canonical_resources(self):
        counter = 0
        for r in self.get_canonical_resources():
            counter += 1
        return counter

    def has_canonical_resources(self):
        if self.num_canonical_resources() == 0:
            return False
        return True

    def depends_on_services(self):
        """
        returns true if there is a service in another
        domain that a resource in this domain depends on.
        """
        if self.num_services_depended_on() > 0:
            return True
        return False
    
    def num_services_depended_on(self):
        """
        returns the number of services in other domains
        that are depended on by a resource in this domain.
        """
        return len(self.get_services_depended_on())

    def get_services_depended_on(self):
        """
        returns the services from other domains
        that this domain depends on.

        This is defined as integration patterns, such as
        ResolutionRequest, between canonical or authorative
        resources in this domain, and some canonical resource
        in anoter domain (which may manifest as a referential
        resource in that other domain)
        """
        found = []
        for r in self.get_resources():
            if r.get_type() != "Referential":
                for s in r.get_services_consumed():
                    if s not in found:
                        found.append(s)
        return found

    def is_depended_on(self):
        """
        returns True if there are services in other
        domins that depend on a service in this domain.
        """
        if self.num_services_that_depend_on() > 0:
            return True
        return False
    
    def num_services_that_depend_on(self):
        """
        returns the number of services in other domains
        that depend on resources in this domain.
        """
        return len(self.get_services_that_depend_on())

    def get_services_that_depend_on(self):
        """
        returns the services in other domains that
        depend on resources in this domain.

        This is defined as integration patterns, such as
        ResolutionRequest, between a canonical resource in
        this domain and resources (canonical or authorative)
        in other domains that depend on them.
        """
        found = []
        for r in self.get_resources():
            if r.get_type() == "Referential":
                if r.ref not in found:
                    found.append(r.ref)
        return found

    def get_domains_that_depend_on(self):
        found = []
        for s in self.get_services_that_depend_on():
            d = s.get_domain()
            if d not in found:
                found.append(d)
        return found

    def num_domains_that_depend_on(self):
        return len(self.get_domains_that_depend_on())

    def num_domains_depended_on(self):
        return len(self.get_domains_depended_on())

    def get_domains_depended_on(self):
        found = []
        for s in self.get_services_depended_on():
            print(s)  # DEBUG
            domain = s.get_domain()
            if domain not in found:
                found.append(domain)
        return found

    def get_resource_refs(self):
        found = []
        for r in self.get_resources():
            if r.get_type() == "Referntial":
                if r.ref not in found:
                    found.append(r.ref)
        return found

    def get_num_resource_refs(self):
        return len(self.get_resource_refs())
    
    def add_resource(self, resource):
        if resource not in self._resources:
            self._resources.append(resource)

    def get_resources(self):
        return self._resources

    # TODO: get_*, has_*, tests

    def __str__(self):
        return self.label
