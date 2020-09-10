from flask_restful import Resource

from service.Acao_service import AcaoService

class AcaoById(Resource):

    def get(self, nome):
        """
        Search in  Acao by the filed nome

        #Read
        """
        service = AcaoService()
        return service.find(None, nome)

    def delete(self, nome):
        """
        Delete a record of Acao

        #Write
        """
        service = AcaoService()
        return service.delete([nome])
