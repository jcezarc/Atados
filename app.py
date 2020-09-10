# -*- coding: utf-8 -*-
import logging
from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from util.swagger_generator import FlaskSwaggerGenerator
from model.Acao_model import AcaoModel
from resource.Acao_by_id import AcaoById
from resource.all_Acao import AllAcao
from model.Voluntario_model import VoluntarioModel
from resource.Voluntario_by_id import VoluntarioById
from resource.all_Voluntario import AllVoluntario
from model.Pessoa_model import PessoaModel
from resource.Pessoa_by_id import PessoaById
from resource.all_Pessoa import AllPessoa


BASE_PATH = '/Atados'

def config_routes(app):
    api = Api(app)
    #--- Resources: ----
    api.add_resource(AcaoById, f'{BASE_PATH}/Acao/<nome>', methods=['GET'], endpoint='get_Acao_by_id')
    api.add_resource(AllAcao, f'{BASE_PATH}/Acao', methods=['GET'], endpoint='get_AllAcao')
    api.add_resource(AllAcao, f'{BASE_PATH}/Acao', methods=['POST'], endpoint='post_Acao')
    api.add_resource(AllAcao, f'{BASE_PATH}/Acao', methods=['PUT'], endpoint='put_Acao')
    api.add_resource(AcaoById, f'{BASE_PATH}/Acao/<nome>', methods=['DELETE'], endpoint='delete_Acao')
    api.add_resource(VoluntarioById, f'{BASE_PATH}/Voluntario/<id>', methods=['GET'], endpoint='get_Voluntario_by_id')
    api.add_resource(AllVoluntario, f'{BASE_PATH}/Voluntario', methods=['GET'], endpoint='get_AllVoluntario')
    api.add_resource(AllVoluntario, f'{BASE_PATH}/Voluntario', methods=['POST'], endpoint='post_Voluntario')
    api.add_resource(AllVoluntario, f'{BASE_PATH}/Voluntario', methods=['PUT'], endpoint='put_Voluntario')
    api.add_resource(VoluntarioById, f'{BASE_PATH}/Voluntario/<id>', methods=['DELETE'], endpoint='delete_Voluntario')
    api.add_resource(PessoaById, f'{BASE_PATH}/Pessoa/<nome>', methods=['GET'], endpoint='get_Pessoa_by_id')
    api.add_resource(AllPessoa, f'{BASE_PATH}/Pessoa', methods=['GET'], endpoint='get_AllPessoa')
    api.add_resource(AllPessoa, f'{BASE_PATH}/Pessoa', methods=['POST'], endpoint='post_Pessoa')
    api.add_resource(AllPessoa, f'{BASE_PATH}/Pessoa', methods=['PUT'], endpoint='put_Pessoa')
    api.add_resource(PessoaById, f'{BASE_PATH}/Pessoa/<nome>', methods=['DELETE'], endpoint='delete_Pessoa')
    
    #-------------------

def set_swagger(app):
    swagger_url = '/docs'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        '/api',
        config={
            'app_name': "*- Atados -*"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


def swagger_details(args):
    id_route = args[0]
    params = args[1]
    model = None
    resource = None
    docstring = ""
    if id_route == 'docs':
        docstring = """Swagger documentation
        #Doc
        """
    elif id_route == 'Acao':
        if not params:
            resource = AllAcao
        else:
            resource = AcaoById
        model = AcaoModel()
    elif id_route == 'Voluntario':
        if not params:
            resource = AllVoluntario
        else:
            resource = VoluntarioById
        model = VoluntarioModel()
    elif id_route == 'Pessoa':
        if not params:
            resource = AllPessoa
        else:
            resource = PessoaById
        model = PessoaModel()
    
    ignore = False
    return model, resource, docstring, ignore

logging.basicConfig(
    filename='Atados.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

APP = Flask(__name__)
CORS(APP)
config_routes(APP)
set_swagger(APP)

@APP.route('/api')
def get_api():
    """
    API json data

    #Doc
    """
    generator = FlaskSwaggerGenerator(
        swagger_details,
        None
    )
    return jsonify(generator.content)

@APP.route('/health')
def health():
    return 'OK', 200


if __name__ == '__main__':
    APP.run(debug=True)
