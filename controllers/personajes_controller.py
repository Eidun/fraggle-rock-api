from flask_restful import Resource
from flask_restful import request

from services import personajes_manager


def parse_args(f):
    def decorated_function(*args, **kwargs):
        json = request.get_json()
        if json is None:
            json = {}
        json['tabla'] = 'PERSONAJES'
        json['id'] = 'entidad_id'
        return f(*args, **kwargs, json=json)
    return decorated_function


class Personajes(Resource):

    @parse_args
    def get(self, json):
        personajes = personajes_manager.get_personajes()
        return personajes, 200

    @parse_args
    def post(self, json):
        personaje = personajes_manager.create_personaje(json)
        return personaje, 200


class Personaje(Resource):

    @parse_args
    def get(self, personaje_id, json):
        json['personaje_id'] = personaje_id
        personaje = personajes_manager.get_personaje(json)
        return personaje, 200

    @parse_args
    def put(self, personaje_id, json):
        json['personaje_id'] = personaje_id
        personaje = personajes_manager.update_personaje(json)
        return personaje, 200

    @parse_args
    def delete(self, personaje_id, json):
        json['personaje_id'] = personaje_id
        personaje = personajes_manager.delete_personaje(json)
        return personaje, 200


