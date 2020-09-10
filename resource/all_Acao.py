import json
from flask_restful import Resource
from flask import request, jsonify
from service.Acao_service import AcaoService

class AllAcao(Resource):

    def get(self):
        """
        Returns all records from the table Acao

        #Read
        """
        service = AcaoService()
        return service.find(request.args)
    
    def post(self):
        """
        Write a new record in Acao

        #Write
        """
        req_data = request.get_json()
        service = AcaoService()
        return service.insert(req_data)

    def put(self):
        """
        Updates a record in Acao

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = AcaoService()
        return service.update(req_data)
