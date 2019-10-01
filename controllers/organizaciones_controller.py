from flask_restful import Resource
from flask_restful import request

from services import organizaciones_manager


def parse_args(f):
    def decorated_function(*args, **kwargs):
        json = request.get_json()
        if json is None:
            json = {}
        json['tabla'] = 'ORGANIZACIONES'
        json['id'] = 'entidad_id'
        return f(*args, **kwargs, json=json)
    return decorated_function


class Organizaciones(Resource):

    @parse_args
    def get(self, json):
        organizaciones = organizaciones_manager.get_organizaciones()
        return organizaciones, 200

    @parse_args
    def post(self, json):
        organizacion = organizaciones_manager.create_organizacion(json)
        return organizacion, 200


class Organizacion(Resource):

    @parse_args
    def get(self, organizacion_id, json):
        json['organizacion_id'] = organizacion_id
        organizacion = organizaciones_manager.get_organizacion(json)
        return organizacion, 200

    @parse_args
    def put(self, organizacion_id, json):
        json['organizacion_id'] = organizacion_id
        organizacion = organizaciones_manager.update_organizacion(json)
        return organizacion, 200


