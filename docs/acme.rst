ACME enterprise model
=====================

.. graphviz::

   digraph d {
      node [shape=rectangle]
      edge [arrowhead=crow];
      label = "meta-domain";

      subgraph cluster_dom1 {
         label="Foo Domain";
	 Foo [label="<<DomainEntity>>\n<<canonical>>\nFoo\n\nname = Foo.id"];
	 FooBar [label="<<DomainID>>\n<<authorative>>\nFooBar\n\nname = FooBar.id\nFK: FooID\n[ref: BarID]"];
      }
      Foo -> FooBar;
      
      subgraph cluster_bar {
         label="Bar Domain";
	 Bar [label="<<DomainEntity>>\n<<canonical>>\nBar\n\nname= Bar.id"];
	 FooBarResolutionRequest [label="<<DomainID>>\n<<referential>>\nFooBarResolutionRequest\n\nname = FooBarResolutionRequest.id\n[ref: BarID]\nFK:FooBarID"];
	 Bar -> FooBarResolutionRequest [style=dashed];
      }
      Bar -> FooBar [style=dashed];
      FooBar -> FooBarResolutionRequest [arrowhead=none];
   }


TODO :code:`[[ cog for l in acme.domain_registry.cog_diagram_all_domains() ]]`

.. automodule:: acme
   :members:
   :undoc-members:

Foo
^^^

In the above diagram, we have a domain called **Foo**. Foo is a very simple domain, it has the minimum possible number (1) of possible concepts required to be a valid domain, and to avoid confusion this concept is also called Foo. So two Foos, **Domain Foo** and **DomainEntity Foo**.

**DomainEntity Foo** is comprised of many Foo entities, each with a unique canonical **FooID name**; you might like to draw an analogy with the **DomainEntity VisaApplication** in the **Domain Visa**, which is *almost* unambigously identified throughout the enterprise by some sort of canonical **VisaApplicationID** name.  I say almost because sometimes, perhaps briefly, the Visa domain may be ignorant or wrong about the person represented by a Vias Applicant, even when they think they know the PersonID of their VisaApplicant. 

When people or machines talk about an **Entity Foo** in other domains, they are likely to reffer to them by their canonical **FooID name**. The exception is when they use some other, non-canonical name that exists in the context of a transaction that they are a party to. Contexturalised identifiers do not alter the characteristics (e.g. smell) of the canonical entity to which they may reffer.

The **Domain Foo** also has these things called a FooBar. These are "weak entities" in the traditional sense, because they only exist as part of a Foo. They are called FooBars because they are somewhat like those things that the word *Bar* is used to represent (the Bar concept), but they are really just a component part of a Foo. The FooBar can be identified by it's **FooBarID name**. Because **Domain Foo** is not the fact authority for the Bar concept, but because it is the fact authority of the **DomainID FooBar**, the **FooBarID name** is authorative, but not canonical (or referential).

You might like to make an analogy between FooBar and the **DomainID VisaApplicant** in the **Domain Visa**. A Visa Applicant represents the concept of a person, and the Visa domain is *not* the fact authority of the person concept. However, the Visa domain is the fact authority of VisaApplicants, which are weak entities that only exist as part of a ViasApplication.

Bar
^^^

Like Foo, **Domain Bar** is very simple with only one canonical concept, **DomainEntity Foo**.

One significant difference is that there are no weak entities in the Bar domain; a Bar entity is not composed of multiple types of constituent part.

There is however another **DomainIdentity FooBarResolutionRequest**, identified by it's **FooBarResolutionRequestID name**. This name is a *referential DomainID** because it exists in the Bar domain, and it essentially identifies a FooBar; The **Domain Bar** is not the fact authority for FooBars, so the FooBarResolutionRequestID is a non-authorative DomainIdentifier in the Bar domain.

When a FooBarResolutionRequest is created, it is assigned a FooBarResolutionRequestID immediately. It is also attributed with a FooBarID, which is known at the time of creation because it is part of the transaction context. Specifically, the transaction context is "Request to the Bar domain, from the Foo domain, to resolve the canonical BarID associated with the given FooBarID". Before that request is filled, the BarID is unknown. Some time later, the BarID may become known. Occasionally, it's possible that the BarDomain may change it's mind about the BarID resolition.    
