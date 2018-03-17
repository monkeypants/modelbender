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
      // genesis state{% if resource.state_chart.has_constructor_transitions() %}
      genesis_state [shape=beginpoint, label=""];
      {% for t in resource.state_chart.get_constructor_transitions() %}
      genesis_state -> {{ t.to_state }} [label={{ t.name }}];{% endfor %}{% endif %}
      
      // terminal state{% if resource.state_chart.has_destructor_transitions() %}
      terminal_state [shape=endpoint, label=""];
      {% for t in resource.state_chart.get_destructor_transitions() %}
      {{ t.from_state }} -> terminal_state [label={{ t.name }}];{% endfor %}{% endif %}
      
      // kludge{% for t in resource.state_chart.get_internal_transitions() %}
      {{ t.from_state }} -> {{ t.to_state }} [label={{ t.name }}];{% endfor %}
   }
{% endif %}

Entity / Relationship Diagram
-----------------------------

TODO: insert ERD

