#!/usr/bin/env python
import uuid

from modelbender.repository import memrepo as mr
from modelbender.use_cases import domain_list_use_case as uc

domains = []
for d in range(4):
    domains.append({
        'code': str(uuid.uuid4()),
        'name': 'test domain {}'.format(d)
    })

repo = mr.MemRepo(domains)
use_case = uc.DomainListUseCase(repo)
result = use_case.execute()

print([d.to_dict() for d in result])
