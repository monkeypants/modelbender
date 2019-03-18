#
# An enterprise is modeled as a collection of domains
#


class Domain:
    """
    A domain:
     * is a collection of distinct Services.
     * is the semantic authority of at least one concept
     * provides services related to their semantic authority

    The purpose of the Domain class in the meta model is to
    collect and manage services to the model.
    """
    def __init__(self, enterprise, label):
        enterprise.add_domain(self)
        self.enterprise = enterprise
        self.label = label
        self._services = []
    
    def has_service_named(self, service_name):
        service = self.get_service_named(service_name)
        if service:
            return True
        else:
            return False

    def get_service_named(self, service_name):
        for service in self._services:
            if str(service) == service_name:
                return service
        return False

    def get_enterprise(self):
        return self.enterprise

    def num_services(self):
        return len(self._services)

    def get_canonical_services(self):
        out = []
        for s in self._services:
            if s.get_type().name == "Canonical":
                out.append(s)
        return out

    def num_canonical_services(self):
        counter = 0
        for r in self.get_canonical_services():
            counter += 1
        return counter

    def has_canonical_services(self):
        if self.num_canonical_services() == 0:
            return False
        return True

    def depends_on_services(self):
        """
        returns true if there is a service in another
        domain that a service in this domain depends on.
        """
        if self.num_services_depended_on() > 0:
            return True
        return False
    
    def num_services_depended_on(self):
        """
        returns the number of services in other domains
        that are depended on by a service in this domain.
        """
        return len(self.get_services_depended_on())

    def get_services_depended_on(self):
        """
        returns the services from other domains
        that this domain depends on.

        This is defined as integration patterns, such as
        ResolutionRequest, between canonical or authorative
        services in this domain, and some canonical service
        in anoter domain (which may manifest as a referential
        service in that other domain)
        """
        found = []
        for s in self.get_services():
            if s.get_type() != "Referential":
                for c in s.get_services_consumed():
                    if c not in found:
                        found.append(c)
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
        that depend on services in this domain.
        """
        return len(self.get_services_that_depend_on())

    def get_services_that_depend_on(self):
        """
        returns the services in other domains that
        depend on services in this domain.

        This is defined as integration patterns, such as
        ResolutionRequest, between a canonical service in
        this domain and services (canonical or authorative)
        in other domains that depend on them.
        """
        found = []
        for s in self.get_services():
            if s.get_type() == "Referential":
                if s.ref not in found:
                    found.append(s.ref)
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
            domain = s.get_domain()
            if domain not in found:
                found.append(domain)
        return found

    def get_service_refs(self):
        found = []
        for s in self.get_services():
            if s.get_type() == "Referntial":
                if s.ref not in found:
                    found.append(s.ref)
        return found

    def get_num_service_refs(self):
        return len(self.get_service_refs())
    
    def add_service(self, service):
        if service not in self._services:
            self._services.append(service)

    def get_services(self):
        return self._services

    def get_resources(self):
        # FIXME: service/resource confusion
        return self._services
    
    # TODO: get_*, has_*, tests

    def __str__(self):
        return self.label
