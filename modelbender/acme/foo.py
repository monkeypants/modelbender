from modelbender.metamodel.domain import Domain
from modelbender.metamodel.state import create_statechart
from modelbender.metamodel.resource import (
    CanonicalResource,
    AuthorativeResource,
    ReferentialResource)
from . import ACMEEnterprise

FooDomain = Domain(ACMEEnterprise, "Foo")

#
# all foos are created happy
# they are never destroyed
#
foo_transition_list = (
    (None, "Happy"),
    ("Happy", "Sad"),
    ("Happy", "Angry"),
    ("Sad", "Happy"),
    ("Sad", "Angry"),
    ("Sad", "Woefull"),
    ("Woefull", "Sad"),
    ("Angry", "Sad"),
    ("Angry", "Happy"),
    ("Angry", "Epperplectic"),
    ("Epperplectic", "Angry"))

#
# TODO: make canonical resource constructor on Domain
# (so no need to pass in FooDomain here)
# domain.register_canonical_resource(name, transition_list)
#
FooResource = CanonicalResource(
    "Foo", FooDomain, foo_transition_list)

# foobars can be created "on" or "of"
# if "fubar" they can be destroyed
foobar_transition_list =(
    (None, "on"), (None, "off"), ("on", "off"),
    ("off", "on"), ("on", "fubar"), ("off", "fubar"),
    ("fubar", None))

#
# TODO: make authorative resource constructor on Domain
# domain.register_authorative_resource(name, transition_list)
# foobar = domain.get_resource("FooBar")
# foo = domain.get_resource("Foo")
# foobar.add_parent(foo)
# foobar.add_identifier("BarID")
# ...
# from service_patterns import ResolutionRequest
# integrations = (
#     ResolutionRequest(
#         bar_domain.bar,
#         foo_domain.foobar,
#         "BarID"),
# ...
FooBarResource = AuthorativeResource(
    "FooBar", foobar_transition_list)

#
# a FooBar is always associated with a Foo
# FooBarResources is Authorative
# this means it can have parent/child relationships
# with CanonicalResources
#
# TODO: do we allow nesting lineage of authorative
# resources, if the tree has a canonical resoure root?
#
FooBarResource.add_parent(FooResource)

#
# it has an optionaly null identifier called "BarID"
# do we really need this?
#
FooBarResource.register_identity("BarID")

#
# we need to document the dependancy here, something
# along the lines of... 
#
# FIXME: FooBarResource.has_resolution_dependancy("BarID", Bar.BarResource)
#
# that should actually create (or update, if it already exists)
# a ReferentialResource in Bar, called "{}{}".format(FooBar, Bar)
#
# That could actually create (by implication) the BarID identity
# too, obviating the need for the register_identity() call.
#
