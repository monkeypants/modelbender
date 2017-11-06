from acme.foo import Foo
# Subscription
##############
# error if resource subscribed_to is not canonical
# implies all the **global subscription pattern** behavior
#
# can be None (for all events)
#
# TODO: this sets up a listener on FooBarResource, that is
# subscribed to all "update" events on the BarResource, where
# the BarResource.identifier matches the FooBarResource.BarID
#
event_filter = ("updated",)
FooBarResource.subscribes_to(
    BarResource,
    event_filter,
    fk="BarID")

