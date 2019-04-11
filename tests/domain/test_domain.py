import uuid
from modelbender.domain import domain as d


def test_domain_model():
    code = uuid.uuid4()
    domain = d.Domain(code, name="test domain")
    assert code == domain.code
    assert domain.name == "test domain"


def test_domain_from_dict():
    code = uuid.uuid4()
    domain = d.Domain.from_dict(
        {
            'code': code,
            'name': 'test domain'
        }
    )
    assert domain.code == code
    assert domain.name == 'test domain'


def test_domain_model_to_dict():
    domain_dict = {
        'code': uuid.uuid4(),
        'name': 'test domain'
    }
    domain = d.Domain.from_dict(domain_dict)
    assert domain.to_dict() == domain_dict


def test_domain_model_comparison():
    domain_dict = {
        'code': uuid.uuid4(),
        'name': 'test domain'
    }
    d1 = d.Domain.from_dict(domain_dict)
    d2 = d.Domain.from_dict(domain_dict)
    assert d1 == d2

