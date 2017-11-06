"""
simple wrapper over the messages that the CLI publishes
"""
class Messenger:
    def __init__(self, DEBUG):
        self.DEBUG = DEBUG

    def invalid_yaml(self, fname):
        if self.DEBUG:
            print("invalid yaml: {}".format(fname))

    def domain_found(self, dk):
        if self.DEBUG:
            print("enterprise.yaml contains domain: {}".format(dk))

    def domain_path(self, fname):
        if self.DEBUG:
            print("enterprise.yaml contains domain: {}".format(fname))

    def domain_without_resources(self, dk):
        if self.DEBUG:
            print("{} has no resources".format(dk))

    def resource_without_spec(self, dk, resource):
        if self.DEBUG:
            msg_tmpl = "{}.{} has no spec"
            msg = msg_tmpl.format(self, dk, resource)
            print(msg)

    def resource_without_canonical(self, dk, resource):
        if self.DEBUG:
            msg_tmpl = "{}.{} has not specified canonical ({})"
            msg = msg_tmpl.format(dk, resource, "assume false")
            print(msg)

    def resource_without_references(self, dk, resource):
        if self.DEBUG:
            msg_tmpl = "{}.{} has no cross-domain referencial dependencies"
            msg = msg_tmpl.format(dk, resource)
            print(msg)

    def resource_has_reference(self, dk, resource, value, key):
        if self.DEBUG:
            msg_tmpl = "{}.{} depends on {} ({})"
            msg = msg_tmpl.format(dk, resource, value, key)
            print(msg)
