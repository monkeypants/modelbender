import uuid
import pytest

from modelbender.domain import domain as d
from modelbender.repository import memrepo


@pytest.fixture
def domain_domains():
    domains = []
    for i in range(4):
        domains.append({
            'code': uuid.uuid4(),
            'name': "test domain {}".format(i)
        })
    return domains


def test_repository_list_without_parameters(domain_domains):
    repo = memrepo.MemRepo(domain_domains)

    domains = [d.Domain.from_dict(i) for i in domain_domains]

    assert repo.list() == domains
