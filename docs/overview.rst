Overview
========

Before we begin, to those who have been burned by `Model Driven Architecture`_ let me first apologise, and promise this tool has no such grandiose and fatally flawed plans. This tool does however make use of a meta-model, to describe knowledge about a model of an enterprise, but it does so with a narrow focus.

.. _`Model Driven Architecture`: https://en.wikipedia.org/wiki/Model-driven_architecture

This tool exists to assist with modelling the integration surface of a (potentially complex or very complicated) enterprise. More specifically, it exists to help create a cohesive and consistent REST API surface, by appplying my highly opinionated heuristics about how that should best be done. If you don't like it write your own tool, or convince me to change my opinions and I'll update this one.

Quickstart
----------

TODO:

 * install it (pip install? note OS dependencies - or use docker?)
 * create a configuration directory for your enterprise model, change into it
 * intialise an enterprise model, :code:`> model-bender init`, talk to the wizard
 * run the generation tool, :code:`> model-bender generate`, see the summary
 * inspect _generated/docs/_build/html/index.html
 * inspect _generated/mocks/docker-compose.yml
 * inspect _generated/tests/_build/html/index.html
 * inspect _generated/simulator/_build/html/index.html

.. note::

   The tests pass against the mocks, but they should also pass
   against any other implementation (including alternate mocks)
   that comply with the docs


Learn More
----------

TODO:

 * the types of resources, iterate your model
 * state machines and events! iterate your model
 * use your mocks in a dynamic enterprise simulation (jupyter)!

