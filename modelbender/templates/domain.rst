{{ domain }}
{% for z in domain.__str__() %}={% endfor %}

This is a page about {{ domain }}. TODO: make it more better. (overview text here)

TODO: diagram: show "depends on" and "is depended on" with resources in other domains

TODO: summary/list of resources this domain depends on

TODO: summary/list of resources in this domain that are depended on by other domains


.. toctree::
   :glob:
   :maxdepth: 1

   {{ domain }}/*

