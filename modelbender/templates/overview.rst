Overview
========

This model of the {{ ctx }} enterprise exists for the purpose of
describing the integration surface. The model is technology agnostic,
however the modelling exercise is being performed for the purpose of
evaluating a REST API architecture driven by an enterprise event
framework.

The model has a static view, which describes the enterprise as a
collection of **domains**. Each domain has a collection of
**resources**, and those resources have logical **interfaces**.

This static view is also enriched with a dynamic model that has
two complimentary aspects:

 * Resource **state**; each resource is considered a *state
   machine* associated with a set of rules about allowable
   *state transitions*. These rules are called the *state
   chart* of the resource.
 * Resource **events**; each resource is attributed with
   a set of possible events that it can *publish*. These
   events corespond to the changes in state allowed by the
   *state chart* for that resource.

The integration strategy is assumed combine an active event
(publish/subscribe) part that compliments a reactive interface
model. Based on this assumption, we have applied minimal
standardised **integration patterns**. These define consistent
approach to data and semantic governance for resources.

Each pattern works by classifying resources into *types*,
documenting business *dependencies* between resources, then
applying policies (based on dependencies between types)
consistently between domains.
