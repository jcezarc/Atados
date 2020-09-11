import sys
sys.path.append('..')
from service.Voluntario_service import VoluntarioService
from model.Voluntario_model import VoluntarioModel, PK_DEFAULT_VALUE
from util.db.fake_table import FakeTable
from util.messages import resp_ok, resp_not_found, GET_NOT_FOUND_MSG

def test_find_success():
    table = FakeTable(VoluntarioModel)
    record = table.default_values()
    table.insert(record)
    service = VoluntarioService(table)
    status_code = service.find(None, PK_DEFAULT_VALUE)[1]
    assert status_code == 200

def test_find_failure():
    service = VoluntarioService(FakeTable(VoluntarioModel))
    message = service.find(None, 999)[0]['status']
    assert message == GET_NOT_FOUND_MSG

def test_insert_success():
    table = FakeTable(VoluntarioModel)
    service = VoluntarioService(table)
    record = table.default_values()
    status_code = service.insert(record)[1]
    assert status_code == 201

def test_insert_failure():
    service = VoluntarioService(FakeTable(VoluntarioModel))
    status_code = service.insert({})[1]
    assert status_code == 400
