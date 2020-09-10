import json
from flask_restful import Resource
from flask import request, jsonify
from service.Voluntario_service import VoluntarioService

class AllVoluntario(Resource):

    def get(self):
        """
        Returns all records from the table Voluntario

        #Read
        """
        service = VoluntarioService()
        return service.find(request.args)
    
    def post(self):
        """
        Write a new record in Voluntario

        #Write
        """
        req_data = request.get_json()
        service = VoluntarioService()
        return service.insert(req_data)

    def put(self):
        """
        Updates a record in Voluntario

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = VoluntarioService()
        return service.update(req_data)
