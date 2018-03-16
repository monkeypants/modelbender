{{ service }}
=========================================

{{ service }} is one of {{ service.domain.num_services() }} services in the {{ service.domain }} domain.

State Chart
-----------

.. blockdiag::

   {{ service }} [shape=roundbox];
   beginpoint -> {{ service }} [label=create];;
   {{ service -> {{ service }} [label=update];
   {{ service }} -> endpoint [label=delete];


Entity / Relationship Diagram
-----------------------------

TODO: insert ERD

