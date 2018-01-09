Meta Model
==========

.. automodule:: modelbender.metamodel


Domain
------

.. autoclass:: modelbender.metamodel.enterprise.Enterprise
   :members:
   :undoc-members:

.. autoclass:: modelbender.metamodel.domain.Domain
   :members:
   :undoc-members:


Resources
---------

Resources are REST API representations of a domain entities. In other words, they are a kind of **Identity** (entity in context). This meta model divides all resources into 3 meta types:

+---------------------------------------+-----------+-------------+-------------+
|                                       | Canonical | Authorative | Referential |
+=======================================+===========+=============+=============+
| Stored in the domain that created it  | True      | True        | False       |
+---------------------------------------+-----------+-------------+-------------+
| Created by the samantic authority     | True      | False       | False       |
+---------------------------------------+-----------+-------------+-------------+
| Managed by the semantic authority     | True      | False       | True        |
+---------------------------------------+-----------+-------------+-------------+


These different types of Resource should be sufficient to classify all the resources defined in an enterprise model.

.. autoclass:: modelbender.metamodel.resource.CanonicalResource
   :members:
   :undoc-members:


.. autoclass:: modelbender.metamodel.resource.AuthorativeResource
   :members:
   :undoc-members:


.. autoclass:: modelbender.metamodel.resource.ReferentialResource
   :members:
   :undoc-members:


Messages and state
------------------

The meta model represents the concept of data as *state machines* that follow rules layed out in a *state chart*. The state machine emits an events every time it undergoes a *state transition*. 


.. autoclass:: modelbender.metamodel.state.StateMachine
   :members:
   :undoc-members:

.. autoclass:: modelbender.metamodel.state.StateChart
   :members:
   :undoc-members:

.. autoclass:: modelbender.metamodel.state.StateTransition
   :members:
   :undoc-members:


TODO:
 * resource instances have state
 * resources emit events when their state changes
 * the resource state == response to GET resource (poll)
 * resource class knows the initial state (constructor method)
 * All events have an object and a predicate.
 * The object is a name (either canonical, authoratitive or referential).
 * The predicate is a description of the change in state of the object.
 * If the name is canonical, the predicate describes the change in state of Entity.
 * If the name is authoratitive, the predicate describes a change in state of the Identity.
 * If the name is referential, the predicate describes a change in state of the context of the identity (e.g transaction or service)



Global Events
^^^^^^^^^^^^^

A **Global Event** is ostensensiably published by the canonical REST resource. In our ACME example, the FooResource and BarResource are the only canonical resources, so they are the only objects that emit global events.

In general, if you wanted to know remain well informed about an DomainEntity (concept) you subscribe to the global event. However...


Service Events
^^^^^^^^^^^^^^

Authorative and referntial resources exist in some business context.

An Authorative resource exists in the context of *a different domain to the natural home of the concept*. For example, a Visa Applicant exists in the Application domain, even though it's a kind of person, and it's natural home of the person concept is some other domain.

A referential resource is even stranger. It ph
e.g. a transaction or service. These services are *directed*, meaning they have both a producer and a consumer (and being a producer is not the same thing as being a consumer).

Authorative DomainIDs belong to a service consumer. Referential DomainIDs belong to a service producer

When the Foo domain creates a FooBar, they attribute it with stuff that they are responsible for based on what they know about the world. Because a FooBar is very much a Bar-like sort of thing, the Foo domain wants to know what BarID each FooBar should be mapped to. This is not something they are responsible for (the Bar domain is responsible for matters Bar). So the Foo domain *consumes* a FooBar resolution service that is *produced* by the Bar domain.

 * **DomainID FooBar** has an authoratitive **FooBarID name**, as part of the **Domain Foo**
 * Foo domain *consumes* a Bar resolution service by calling ``POST {FooBarDetails} /FooBarResolutionRequests`` (to the Bar domain)
 * Bar domain *produces* a Bar resolution service by accepting the request and creating a referntial *DomainID FooBarResolutionRequest* , then asynchronously processing the request.

At the sucessful conclusion of the service provision, the producer (**Domain Bar**) will emits a service event, from the referntial **name FooBarResolutionRequest**. One assumes the service consumer, **name FooBar** in the **Domain Foo** has subscribed. If the results of the FooBarResolutionService are part of the public data of the canonical **BarID named resource**, then we would expect the Bar to emit a global event as well (otherwise, we would not)

However unlikely/rare, if the Bar domain changed it's mind about the Bar resolution of the FooBar, this might manifest as an update to the state of the FooBarResolutionRequest named resource. In this case, we would expect the FooBarResolutionRequest to emit another service message (producer message, predicate=update?), and *if they still care*, the FooBar would be subscribed to that service event. This also may or may not have an associated global event (depending on if the list of FooBarResolutionRequests was part of the public interface of the Bar).

Also, if the Foo domain recieved new information about the FooBar, it might want to tell the Bar domain about it (maybe the new information is material to the Bar resolution?). In that case, it would send a FooBar service consumer message, and presumably (if they cared) the service provider would be subscribed to it.


Event Identifiers
^^^^^^^^^^^^^^^^^

Events are *identifiers* of *state transitions* of *resources*. In other words, they have names. The names are coded into a topic and an ID. The ID is a meaningless string with the property of uniqueness.

.. event ID should be a multihash of the full resource state!

The topic is composed of a {resource}.{predicate}.

The {status} part is the name of the transition (e.g. from stateA to stateB) from the StateChart associated with the resource. The state chart may have many transitions, but exactly one of them was the triger of the event - that's the event predicate.

.. we need transitions from and to None state, probably called "create" and "delete"

The {resource} part is one of the names of the resource. The resource will have a URL, which is nice, but it's not what we put in the event topic. Instead, we make a name like {domain}.{resource}.{id}

So a full topic looks like this: {domain}.{resource}.{id}.{predicate}


Event Status
^^^^^^^^^^^^

The *state* of a resource is exactly what you get when you GET the resource. Let's imagine it as a something like a json document (although, the same state could be encoded in multiple formats). It may contain many data attributes. It is resource "instance data".

An event *status* represents the current state machine abstraction, associated with the state chart. The state chart is class data, not instance data. The status of the resource is instance data (that contribute's the the instance date, but is not the only constituent).
