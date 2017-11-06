from modelbender.metamodel.domain import Domain
from modelbender.metamodel.state import create_statechart
from modelbender.metamodel.resource import (
    CanonicalResource,
    AuthorativeResource,
    ReferentialResource
)
from . import ACMEEnterprise

BarDomain = Domain(ACMEEnterprise, "Bar")

bar_transition_list = (
    (None, "missing"),
    (None, "found"),
    ("missing", "found"),
    ("found", "missing"))

BarResource = CanonicalResource(
    "Bar",
    BarDomain,
    bar_transition_list)


#-- Foo
#
# should be created by inference of the subscription!
# (side effect of code in foo.py)
# combined with modelbender.service_patterns.ResolutionRequest
transition_list = (
    (None, "unresolved"),
    ("unresolved", "updated_unresoved"),
    ("unresolved", "resolved"),
    ("updated_unresolved", "resolved"),
    ("resolved", "updated_resolved"),
    ("updated_resolved", "updated_resolved"), 
    ("updated", None),
    ("updated_resolved", None))

# name like "{}{}{}".fomrat(domain, resource, pattern)
FooBarResolutionRequest = ReferentialResource(
    "FooBarResolutionRequest",
    BarDomain, BarResource,
    transition_list)
