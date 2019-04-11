import uuid
from enterprise_architecture.domain import domain as d


def test_domain_model_init():
    code = uuid.uuid4()
    domain = d.Domain(code, name="test domain")
    assert domain.code == code
    assert domain.name == "test domain"
