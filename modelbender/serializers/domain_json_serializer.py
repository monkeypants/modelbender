import json


class DomainJsonEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'code': str(o.code),
                'name': str(o.name)
            }
            return to_serialize
        except AttributeError:
            return super().default(o)

        
