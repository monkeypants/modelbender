import pytest
import uuid
from unittest import mock

from modelbender.domain import domain as d
from modelbender.use_cases import domain_list_use_case as uc


@pytest.fixture
def domain_domains():
    domains = []
    for i in range(4):
        domains.append(
            d.Domain(
                code=uuid.uuid4(),
                name="test domain {}".format(i)
            )
        )
    return domains


def test_domain_list_without_parameters(domain_domains):
    repo = mock.Mock()
    repo.list.return_value = domain_domains

    domain_list_use_case = uc.DomainListUseCase(repo)
    result = domain_list_use_case.execute()

    repo.list.assert_called_with()
    assert result == domain_domains
