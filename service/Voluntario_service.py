import logging
from model.Voluntario_model import VoluntarioModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table

class VoluntarioService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(VoluntarioModel)

    def find(self, params, id=None):
        if id:
            logging.info(f'Finding "{id}" in Voluntario ...')
            found = self.table.find_one([id])
        else:
            logging.info('Finding all records of Voluntario...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('New record write in Voluntario')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok()

    def update(self, json):
        logging.info('Changing record of Voluntario ...')
        errors = self.table.update(json)
        if errors:
            return resp_error(errors)
        return resp_ok("Record changed OK!")
        
    def delete(self, id):
        logging.info('Removing record of Voluntario ...')
        self.table.delete(id)
        return resp_ok("Deleted record OK!")
