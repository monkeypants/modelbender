The {{ctx}} Domain
==========={% for i in ctx.__str__() %}={% endfor %}

The {{ ctx }} domain has {{ ctx.num_resources() }} resources,

.. graphviz::

   digraph d {
      label="resources";
      node [shape=rectangle];
      edge [arrowhead=crow];
      {% for r in ctx.get_resources() %}
      {{ r }} [label="<<{{ r.get_type() }}>>\n{{ r }}"];{% endfor %}
      {% for r in ctx.get_resources() %}{% for p in r.get_parents() %}
      {{ p }} -> {{ r }};{% endfor %}{% endfor %}
   }


{% if ctx.is_depended_on() %}
There are {{ ctx.num_services_that_depend_on() }} services
(from {{ctx.num_domains_that_depend_on() }} domains) that
depend on resources in the {{ ctx }} domain.

TODO: create consultultation/advisory matrix for changes to the
{{ ctx }} domain.
{% else %}
There are no domains that depend on services provided by the
{{ ctx }} domain. That means the {{ ctx }} domain is able to
change it's interfaces without *consulting* any other domains.

{% if ctx.has_canonical_resources() %}
.. note::

   Because the {{ ctx }} domain has {{ ctx.num_canonical_resources() }}
   canonical resources, all other domains must be *informed* about all
   proposed changes to canonical resources.


TODO: create consultultation/advisory matrix for changes to the
{{ ctx }} domain.

{% else %}
{% endif %}{% endif %}
{% if ctx.depends_on_services() %}
The {{ ctx }} domain depends on {{ ctx.num_services_depended_on() }}
external resources from {{ ctx.num_domains_depended_on() }} other domains.

{% else %}
The {{ ctx }} domain does not depend on external services from any
other domain. That means there are no other domains which must consult
with the custodians of the {{ ctx }} domain when they propose changes
to their interfaces.
{% endif %}

TODO: create consultation/advisory matrix for changes that impact
the {{ ctx }} domain.

{% if ctx.is_depended_on() or ctx.depends_on_services() %}
.. graphviz::

   digraph d {
      label="{{ ctx }} in context";
      node [shape=rectangle];
      {{ ctx }} [shape=folder];
      TODO -> {{ ctx }};
      A -> {{ ctx }};
      B -> {{ ctx }};
      {{ ctx }} -> C;
      {{ ctx }} -> D;
   }
{% endif %}

{% for resource in ctx.get_resources() %}

{{ resource }} Resource
---------{% for i in resource.__str__() %}-{% endfor %}

The {{ resource }} is of {{ resource.get_type() }} type.

{% if resource.get_type().__str__() == 'Canonical' %}
This means the resource is semantically authorative.
The {{ resource.get_domain() }} domain has cariage over the
meaning and interpretation of the concept of {{ resource }}
within the {{ resource.get_domain().get_enterprise() }}
enterprise.

It also means that the {{ resource.get_domain() }} domain is
wholy responsible for data associated with the {{ resource }}
resource. It is impossible for other domains to update the
{{ resource }} resource directly (POST, PUT, PATCH or DELETE).
However, they may participate in transactions that indirectly
result in changes to the state of the {{ resource }} resource.

As a Canonical resource, other domains may subscribe to global
events about changes to this resource.

TODO: if this canonical resource has authorative children,
a GET of this resource will include data that changes when
the authorative child resources changes. When the child
authorative resources changes, the canonical resource emits
a message. Spell this out with actual references (if any)
{% endif %}
{% if resource.get_type().__str__() == 'Authorative' %}
TODO: authorative text...
{% endif %}
{% if resource.get_type().__str__() == 'Referential' %}
TODO: referential text
{% endif %}


{% if resource.state_chart.is_populated() %}
{{ resource }} State Chart
^^^^^^^^^^^^{% for i in resource.__str__() %}^{% endfor %}

The {{ resource }} resource has
{{ resource.state_chart.num_concrete_states() }} possible states.
{% if resource.state_chart.has_abstract_states() %}The {{ resource }}
resource state-chart also includes the abstract *null* state.

{% if resource.state_chart.has_constructor_transitions() %}The
state-chart has {{ resource.state_chart.num_constructor_transitions() }}
constructor transitions:
{% for t in resource.state_chart.get_constructor_transitions() %}
 * {{ t.to_state }}{% endfor %}
{% else %}
The state-chart does not include any consturctor transitions. The
process for creating {{ resource }} resources has not been included
in the model state-chart.
{% endif %}
{% if resource.state_chart.has_destructor_transitions() %}The
state-chart has {{ resource.state_chart.num_destructor_transitions() }}
destructor transitions:
{% for t in resource.state_chart.get_destructor_transitions() %}
 * {{ t.to_state }}{% endfor %}
{% else %}
The state-chart does not include any desturctor transitions. The
process for destroying/deleting {{ resource }} resources has not
been included in the model state-chart.
{% endif %}

{% else %}The {{ resource }} resource state chart does not include
the abstract *null* state; The process for creating and destroying
these resources has not been included in the model state-chart.
{% endif %}

.. graphviz::

   digraph d {
      label="{{ resource }} state chart";
      {% for dot_line in resource.state_chart.get_dot_lines() %}
      {{ dot_line }}{% endfor %} 
   }

This state-chart can also be represented as a table of allowable
state transitions.

{% for line in resource.state_chart.get_rst_table_lines() %}
{{ line }}{% endfor %}
{% endif %}

External Dependencies on the {{ resource }} resource
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{% for i in resource.__str__() %}^{% endfor %}

TODO: summary then tree of things that depend on this resource


External services that the {{ resource }} resource depends on
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{% for i in resource.__str__() %}^{% endfor %}

TODO: summary then tree of things that this resource depends on

{% endfor %}
