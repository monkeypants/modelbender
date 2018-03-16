Integration Surface Model for {{ ctx }}
=============================={% for i in ctx.__str__() %}={% endfor %}

Domains:
{% for domain in ctx.get_domains() %}
  * [{{ domain }}](domains/{{ domain }}.md){% endfor %}

