import uuid
import json

from flask import Blueprint, Response

from modelbender.repository import memrepo as mr
from modelbender.use_cases import domain_list_use_case as uc
from modelbender.serializers import domain_json_serializer as ser
blueprint = Blueprint('domain', __name__)

domain_dicts = []
for i in range(4):
    domain_dicts.append({
        'code': str(uuid.uuid4()),
        'name': 'test domain {}'.format(i)
    })

@blueprint.route('/domains', methods=['GET'])
def domain():
    repo = mr.MemRepo(domain_dicts)
    use_case = uc.DomainListUseCase(repo)
    result = use_case.execute()

    return Response(
        json.dumps(result, cls=ser.DomainJsonEncoder),
        mimetype='application/json',
        status=200
    )
