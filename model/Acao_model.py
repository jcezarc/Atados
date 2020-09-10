from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean


PK_DEFAULT_VALUE = "000"

class AcaoModel(Schema):
    nome = Str(primary_key=True, default=PK_DEFAULT_VALUE, required=True)
    instituicao = Str()
    local = Str()
    descricao = Str()


