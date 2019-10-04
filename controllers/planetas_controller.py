from flask_restful import Resource
from flask_restful import request

from services import planetas_manager


def parse_args(f):
    def decorated_function(*args, **kwargs):
        json = request.get_json()
        if json is None:
            json = {}
        json['tabla'] = 'PLANETAS'
        json['id'] = 'lugar_id'
        return f(*args, **kwargs, json=json)

    return decorated_function


class Lugares(Resource):

    @parse_args
    def get(self, json):
        planetas = planetas_manager.get_planetas()
        return planetas, 200

    @parse_args
    def post(self, json):
        planeta = planetas_manager.create_planeta(json)
        return planeta, 200


class Lugar(Resource):

    @parse_args
    def get(self, planeta_id, json):
        json['planeta_id'] = planeta_id
        planeta = planetas_manager.get_planeta(json)
        return planeta, 200

    @parse_args
    def put(self, planeta_id, json):
        json['planeta_id'] = planeta_id
        print(json)
        planeta = planetas_manager.update_planeta(json)
        return planeta, 200
