Domains
=======

The {{ ctx }} enterprise is made up of {{ ctx.num_domains() }} domains.

.. graphviz::

   digraph d {
      node [shape="folder"];
      rankdir=LR;
      subgraph cluster_x {
         label = "{{ ctx }}"
	 {% for d in ctx.get_domains() %}
         {{ d }} [label="{{ d }} Domain ({{ d.num_resources() }} resources)"];{% endfor %}
      }
   }


TODO: table of people (names, email, etc) in role for each domain
   
.. toctree::

{% for d in ctx.get_domains() %}   {{ d }}
{% endfor %}
