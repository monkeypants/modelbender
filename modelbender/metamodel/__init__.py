"""
We need to model a big complicated enterprise, we need an
**enterprise model**.

We want to use that model to define the integration surface
of it's constituent parts (using REST API concepts). We will
use our enterprise model to inform our **API surface**. We
will this API surface to manage the delivery, support and
integration of our enterprise services.

We do not want the enterprise model to be more complicated
than necessary. The model-bender solution is to use some
simple patterns that are applied consistently to the various
parts of the enterprise.

I'm going to call this simple pattern the "meta model". It's a
model of knowledge about the model of the enterprise. Sorry if
that does your head in, I really will try to keep it simple.

.. graphviz::

   digraph d {
     node [shape=folder style=filled fillcolor=lightgrey];
     subgraph cluster_logical {
        label=logical;
        mm [label="meta model" fillcolor=green];
        em [label="enterprise model" fillcolor=white];
     }
     subgraph cluster_physical {
        label=physical;
        srv [label="enterprise services"];
        app [label="API surface" fillcolor=white];
        data;
     }
     app -> em -> mm;
     app -> srv -> data;
     srv -> em;
   }


The meta model talks in general terms about **domains**,
**resources** and **events**. It defines a handful of
different types of resources and events, and makes rules
about the types of events those types of resource can
publish and subscribe to.

Because the enterprise model inherits these rules and
patterns from the meta model, we can use inference to 
generate specifications and other documentation, and even
automated tests of services.
"""
pass
