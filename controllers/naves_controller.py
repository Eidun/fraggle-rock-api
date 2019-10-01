from flask_restful import Resource
from flask_restful import request

from services import naves_manager


def parse_args(f):
    def decorated_function(*args, **kwargs):
        json = request.get_json()
        if json is None:
            json = {}
        json['tabla'] = 'NAVES'
        json['id'] = 'id'
        return f(*args, **kwargs, json=json)
    return decorated_function


class Naves(Resource):

    @parse_args
    def get(self, json):
        naves = naves_manager.get_naves()
        return naves, 200

    @parse_args
    def post(self, json):
        nave = naves_manager.create_nave(json)
        return nave, 200


class Nave(Resource):

    @parse_args
    def get(self, nave_id, json):
        json['nave_id'] = nave_id
        nave = naves_manager.get_nave(json)
        return nave, 200

    @parse_args
    def put(self, nave_id, json):
        json['nave_id'] = nave_id
        print(json)
        nave = naves_manager.update_nave(json)
        return nave, 200


