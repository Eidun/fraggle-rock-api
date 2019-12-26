from db.impl import db_personajes, db_organizaciones
from db import transaction
from db import db_utils


@transaction
def get_personajes(db):
    personajes = db_personajes.get_personajes(db)
    return personajes


@transaction
def get_personaje(db, json):
    personaje = db_personajes.get_personaje(db, json['personaje_id'])
    if personaje['organizacion_id'] is not None:
        personaje['organizacion'] = db_organizaciones.get_organizacion(db, personaje['organizacion_id'])
    return personaje


@transaction
def create_personaje(db, json):
    personaje = db_personajes.create_personaje(db, json)
    __update_personaje(db, personaje, json)
    return personaje


@transaction
def update_personaje(db, json):
    personaje = db_personajes.get_personaje(db, json['personaje_id'])
    if json['alias'] is not None:
        db_utils.update_simple_field(db, 'ENTIDADES', 'alias', json['alias'], 'id', personaje['id'])
        personaje['alias'] = json['alias']
    __update_personaje(db, personaje, json)
    return personaje


def __update_personaje(db, personaje, json):
    for change in json['data']:
        db_utils.update_simple_field(db, table_name=json['tabla'], field_name=change['field'], value=change['value'],
                                     id_name=json['id'], id_value=personaje['id'])
        personaje[change['field']] = change['value']
    return personaje

@transaction
def delete_personaje(db, json):
    personaje = db_personajes.get_personaje(db, json['personaje_id'])
    db_utils.delete_simple_row(db, 'PERSONAJES', 'entidad_id', personaje['id'])
    db_utils.delete_simple_row(db, 'ENTIDADES', 'id', personaje['id'])
    __delete_personaje(db, personaje, json)
    return personaje


def __delete_personaje(db, personaje, json):
    db_utils.delete_simple_row(db, table_name=json['tabla'], id_name=json['id'], id_value=personaje['id'])
    return personaje
