from flask_restful import Resource
from flask_restful import request

from services import entidades_manager


def parse_args(f):
    def decorated_function(*args, **kwargs):
        json = request.get_json()
        if json is None:
            json = {}
        json['tabla'] = 'ENTIDADES'
        json['id'] = 'id'
        return f(*args, **kwargs, json=json)
    return decorated_function


class Entidades(Resource):

    @parse_args
    def get(self, json):
        entidades = entidades_manager.get_entidades()
        return entidades, 200
