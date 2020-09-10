from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Pessoa_model import PessoaModel
from model.Acao_model import AcaoModel


PK_DEFAULT_VALUE = 0

class VoluntarioModel(Schema):
    id = Integer(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    inicio = Date()

    pessoa = Nested(PessoaModel)
    acao = Nested(AcaoModel)

