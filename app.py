#!flask/bin/python
from flask import Flask
from flask_restful import Api
from controllers.entidades_controller import Entidades
from controllers.lugares_controller import Lugares, Lugar
from controllers.naves_controller import Naves, Nave
from controllers.personajes_controller import Personajes, Personaje
from controllers.organizaciones_controller import Organizaciones, Organizacion
from flask_cors import CORS, cross_origin
app = Flask(__name__)
api = Api(app)
cors = CORS(app)

api.add_resource(Entidades, '/entidades')
api.add_resource(Personajes, '/personajes')
api.add_resource(Personaje, '/personajes/<personaje_id>')
api.add_resource(Organizaciones, '/organizaciones')
api.add_resource(Organizacion, '/organizaciones/<organizacion_id>')
api.add_resource(Naves, '/naves')
api.add_resource(Nave, '/naves/<nave_id>')
api.add_resource(Lugares, '/lugares')
api.add_resource(Lugar, '/lugares/<lugar_id>')


if __name__ == '__main__':
    app.run(debug=True)
