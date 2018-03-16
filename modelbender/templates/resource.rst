{{ resource }}
=========================================

**{{ resource }}** is one of {{ resource.domain.num_services() }} services in the {{ resource.domain }} domain.


{% if resource.state_chart.is_populated() %}
State Chart
-----------

.. blockdiag::

   blockdiag {{ resource }} {
      orientation=portrait;
      // non-entrant states{% for state in resource.state_chart.get_concrete_states() %}
      {{ state }} [shape=roundedbox];{% endfor %}
      // genesis state {% if resource.state_chart.has_constructor_transitions() %}
      genesis_state [shape=beginpoint, label=""]; {% endif %}
      // terminal state{% if resource.state_chart.has_destructor_transitions() %}
      terminal_state [shape=endpoint, label=""];{% endif %}
      // kludge
      {{ resource }} [shape=roundedbox];
      {{ resource }} -> {{ resource }} [label=update];
      {{ resource }} -> terminal_state;  // [label=delete];
   }

{% if resource.state_chart.has_concrete_states() %}
{{ resource }} has {{ resource.state_chart.num_concrete_states() }} possible states.
{% for state in resource.state_chart.get_states() %}
 * {{ state }}{% endfor %}
{% endif %}

{% if resource.state_chart.has_constructor_transitions() %}
{{ resource }} has {{ resource.statechart.num_constructor_transitions() }} constructor transitions.
{% for t in resource.state_chart.get_constructor_transitions() %}
 * {{ t }}{% endfor %}
{% endif %}

{% if resource.state_chart.has_destructor_transitions() %}
{{ resource }} has {{ resource.statechart.num_destructor_transitions() }} desstructor transitions.
{% for t in resource.state_chart.get_destructor_transitions() %}
 * {{ t }}{% endfor %}
{% endif %}

{% endif %}


Entity / Relationship Diagram
-----------------------------

TODO: insert ERD

