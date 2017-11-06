from modelbender.metamodel import Enterprise
import ruamel.yaml as yaml


# make this roundtrip
#######################
# python code -> fragmented yaml
# fragmented yaml -> one big yaml
# one big yaml -> dynamic code
# dynamic code + template -> artefacts
#
# because:
#  - writing python code is nicer on the eyes than writing yaml
#  - fragmented yaml is best in a repo, because different teams
#  - one big yaml is easier for validation etc
#  - dynamic code + templates == good
#

#
# define the enterprise with 4 domains
#
acme = Enterprise(
    'ACME',
    tagline="The Company that provides stuff to Wiley Coyotee")

#
sales = acme.add_domain(
    acme, "Sales",
    tagline="People wot sell stuff to Wiley Coyotee")
sales_client = sales.add_resource("Client", canonical=True)
sales_order = sales.add_resource("Order", canonical=True)
sales_order.parent_dependancy(sales_client)
sales_orderitem = sales.add_resource("OrderItem", canonical=False)
sales_orderitem.parent_dependancy(sales_order)

#
marketing = acme.add_domain(
    acme, "Marketing",
    tagline="People wot tell Wiley Coyotee about ACME stuff")
#
manufacturing = acme.add_domain(
    acme, "Manufacturing",
    tagline="People wot make the stuff Wiley Coyotee buys")
manufacturing_product = manufacturing.add_resource("Product", canonical=True)

#
distribution = acme.add_domain(
    acme, "distribution",
    tagline="People wot get the stuff Wiley Coyotee buys to him")
distribution_delivery = distribution.add_resource("Delivery", canonical=True)

# resolution dependancies must be:
#  - from a non-canonical to canonical
#  - between different domains
sales_orderitem.resolution_dependancy(manufacturing_product, "ProductID")

#
# Can we dump the object tree to yaml automatically?
#
with open("enterprise.yaml", "w") as outfile:
    yaml.dump(enterprise, outfile, default_flow_style=False)
    #yaml.dump(enterprise, outfile, default_flow_style=True)

