import logging
from model.Acao_model import AcaoModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class AcaoService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(AcaoModel)

    def find(self, params, nome=None):
        if nome is not None:
            logging.info(f'Finding "{nome}" in Acao ...')
            found = self.table.find_one([nome])
        else:
            logging.info('Finding all records of Acao...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('New record write in Acao')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Changing record of Acao ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Record changed OK!")
        
    def delete(self, nome):
        logging.info('Removing record of Acao ...')
        self.table.delete(nome)
        return resp_ok("Deleted record OK!")
