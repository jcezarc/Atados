from flask_restful import Resource
from service.Voluntario_service import VoluntarioService

class VoluntarioById(Resource):

    def get(self, id):
        """
        Search in  Voluntario by the filed id

        #Read
        """
        service = VoluntarioService()
        return service.find(None, id)

    def delete(self, id):
        """
        Delete a record of Voluntario

        #Write
        """
        service = VoluntarioService()
        return service.delete([id])
