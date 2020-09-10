from flask_restful import Resource

from service.Pessoa_service import PessoaService

class PessoaById(Resource):

    def get(self, nome):
        """
        Search in  Pessoa by the filed nome

        #Read
        """
        service = PessoaService()
        return service.find(None, nome)

    def delete(self, nome):
        """
        Delete a record of Pessoa

        #Write
        """
        service = PessoaService()
        return service.delete([nome])
