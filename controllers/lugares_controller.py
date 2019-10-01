from flask_restful import Resource
from flask_restful import request

from services import lugares_manager


def parse_args(f):
    def decorated_function(*args, **kwargs):
        json = request.get_json()
        if json is None:
            json = {}
        json['tabla'] = 'LUGARES'
        json['id'] = 'id'
        return f(*args, **kwargs, json=json)
    return decorated_function


class Lugares(Resource):

    @parse_args
    def get(self, json):
        lugares = lugares_manager.get_lugares()
        return lugares, 200

    @parse_args
    def post(self, json):
        lugar = lugares_manager.create_lugar(json)
        return lugar, 200


class Lugar(Resource):

    @parse_args
    def get(self, lugar_id, json):
        json['lugar_id'] = lugar_id
        lugar = lugares_manager.get_lugar(json)
        return lugar, 200

    @parse_args
    def put(self, lugar_id, json):
        json['lugar_id'] = lugar_id
        print(json)
        lugar = lugares_manager.update_lugar(json)
        return lugar, 200


