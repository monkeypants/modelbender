from acme.bar import (BarDomain, BarResource)

# this whole thing needs refactoring

#-- Foo
#
# should be created by inference of the subscription
#
transition_list = (
    (None, "unresolved"),
    ("unresolved", "updated_unresoved"),
    ("unresolved", "resolved"),
    ("updated_unresolved", "resolved"),
    ("resolved", "updated_resolved"),
    ("updated_resolved", "updated_resolved"), 
    ("updated", None),
    ("updated_resolved", None))

FooBarResolutionRequest = ReferentialResource(
    "FooBarResolutionRequest",
    BarDomain, BarResource,
    transition_list)


#
# Dependencies
##############
# error if not depending on canonical resource in another domain
# this *implies* the existance of the referntial resource
# referential resource is created as a consequence
# error if service_name already used in depended resource's domain
# this also *implies* all the private subscription behavior associated
# with the **resolution request pattern**
FooBarResource.depends_on(
    FooBarResolutionRequest,
    service_name="FooBarResolutionRequest")


