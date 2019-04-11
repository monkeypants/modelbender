import uuid
import json
from unittest import mock

from modelbender.domain.domain import Domain

domain_dict = {
    'code': str(uuid.uuid4()),
    'name': 'test domain Fred'
}
domain = Domain.from_dict(domain_dict)

domains = [domain]

@mock.patch('modelbender.use_cases.domain_list_use_case.DomainListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = domains
    
    http_response = client.get('/domains')
    
    assert json.loads(http_response.data.decode('UTF-8')) == [domain_dict]
    mock_use_case().execute.assert_called_with()
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'
