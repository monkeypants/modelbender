from modelbender.metamodel.state import StateChart
#
# A domain is modelled as a collection of typed resources.
#
class ResourceType:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def get_summarised_meaning(self):
        return self.description
    def __str__(self):
        return self.name
    
CANONICAL_TYPE = ResourceType(
    "Canonical",
    "Semantically and factually authorative")

class CanonicalResource:
    """
    A canonical resource:
     * represents an identity that logically belongs (semantic authority) to the domain that created it, manages it and stores it.
     * provides an idenifier that is used to reffer to the entity outside of any specific service or transaction context.

    A canonical identity publishes global events, that may be of
    interest to anyone interested in the entity (concept) the canonical
    identity represents.

    A canonical resource is persistent, it's data should be maintained
    in a system of record.
    """
    def __init__(self, label, domain, transition_list=None):
        sc = StateChart()
        if transition_list:
            for from_state, to_state in transition_list:
                sc.add_transition(from_state, to_state)
        self.state_chart = sc
        self.domain = domain
        self.label = label
        self.domain.add_resource(self)
        self._services_consumed = []

    def get_services_consumed(self):
        return self._services_consumed

    def get_domain(self):
        return self.domain

    def get_type(self):
        return CANONICAL_TYPE

    def get_parents(self):
        """
        Canonical resources do not have parents.

        (or belly buttons)
        """
        return ()

    def __str__(self):
        return self.label

# test: ci.get_domain().has_entity(self) == True
# test: for d in domain.get_entities():
#     for e in d.get_entities():
#         d == e.get_domain()

AUTHORATIVE_TYPE = ResourceType(
    "Authorative",
    "Factually (but not semantically) Authorative")

class AuthorativeResource:
    """
    An authorative identity is:
     * an identity that does not strictly belong to the domain 
       (in a logical/semantic sense)
     * an "weak" entity that physically belongs to the domain
     * an identity that is not used globally

    An authorative identity it is only used locally within the
    domain, and in a private service/transaction contexts outside
    the domain.

    What I mean by "weak entity" is that it only exists as part of
    another entity, it is not in any way interesting in and of itself.
    An authorarive identity has a persistent resource, which is probably
    associated (part of) a canonical resource's record (rather than a
    record in it's own right).

    An authorative identity publishes private messages that are only
    relevant/available to service producers that are a party to a
    transaction involving the authorative identity.
    """
    def __init__(self, label, transition_list=None):
        sc = StateChart()
        if transition_list:
            for from_state, to_state in transition_list:
                sc.add_transition(from_state, to_state)
        self.state_chart = sc
        self._parents = []
        self.label = label
        self._services_consumed = []
        self._identities = []

    def get_services_consumed(self):
        return self._services_consumed

    def get_domain(self):
        # note, this supports nesting
        parents = self.get_parents()
        domain_check = None
        for p in parents:
            if not domain_check:
                domain_check = p.get_domain()
            else:
                if p.get_domain() != domain_check:
                    raise Exception(
                        "AuthorativeResource parents of mismatched domain")
        if len(parent) == 0:
            raise Exception("AuthorativeResource has no parent")
        if not self._domain:
            a_parent = parents[0]
            self._domain = a_parent.get_domain()
        return self._domain

    def get_type(self):
        return AUTHORATIVE_TYPE

    def add_parent(self, parent):
        # FIXME: ensure parent is a CanonicalResource
        # or an AuthorativeResource, and that is in
        # the same domain
        self._domain = parent.get_domain()
        if parent not in self._parents:
            self._parents.append(parent)
        self._domain.add_resource(self)

    def get_parents(self):
        return list(self._parents)

    def register_identity(self, identifier):
        if identifier not in self._identities:
            self._identities.append(identifier)

    def __str__(self):
        return self.label


REFERENTIAL_TYPE = ResourceType(
    "Referential",
    "Not factually authorative")

class ReferentialResource:
    """
    A referential identity:
     * does not strictly belong to the domain that  
       (in a logical/semantic sense)
     * is created **by** a service consumer domain
     * is created **in** a service producer domain (does not
       pyhsically belong to the servie consumer domain)
     * is only used in the context of service delivery (not globally)
     * has a refernce to an identity in the service consumer domain

    A referential identity has an ephemeral resource. It need only 
    exists for as long as the service provider domain deems it
    relevant to their service provision.

    An referential identity publishes private messages that are only
    relevant/available to service consumers that are a party to a
    transaction involving the referential identity.
    """
    def __init__(self, domain, label, ref, entity, transition_list=None):
        sc = StateChart()
        if transition_list:
            for from_state, to_state in transition_list:
                sc.add_transition(from_state, to_state)
        self.state_chart = sc
        self.domain = domain
        self.label = label
        self.ref = ref
        self.entity = entity

    def get_domain(self):
        return self.domain

    def get_type(self):
        return REFERENTIAL_TYPE

    def get_parents(self):
        return ()

    def __str__(self):
        return self.label
