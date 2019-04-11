import json
import uuid

from modelbender.serializers import domain_json_serializer as ser
from modelbender.domain import domain as d

def test_serialize_domain_domain():
    code = uuid.uuid4()
    domain = d.Domain(
        code=code,
        name="test domain"
    )
    expected_json = """
        {{
           "code": "{}",
           "name": "test domain"
        }}
    """.format(code)
    json_domain = json.dumps(
        domain,
        cls=ser.DomainJsonEncoder
    )
    loaded = json.loads(json_domain)
    expected = json.loads(expected_json)
    assert loaded == expected


    
