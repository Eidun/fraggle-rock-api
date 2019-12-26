from db.impl import db_organizaciones, db_personajes
from db import transaction
from db import db_utils


@transaction
def get_organizaciones(db):
    organizaciones = db_organizaciones.get_organizaciones(db)
    return organizaciones


@transaction
def get_organizacion(db, json):
    organizacion = db_organizaciones.get_organizacion(db, json['organizacion_id'])
    if organizacion['lider_id'] is not None:
        organizacion['lider'] = db_personajes.get_personaje(db, organizacion['lider_id'])
    organizacion['miembros'] = db_personajes.get_miembros(db, organizacion['id'])
    return organizacion


@transaction
def create_organizacion(db, json):
    organizacion = db_organizaciones.create_organizacione(db, json)
    __update_organizacion(db, organizacion, json)
    return organizacion


@transaction
def update_organizacion(db, json):
    organizacion = db_organizaciones.get_organizacion(db, json['organizacion_id'])
    if json['alias'] is not None:
        db_utils.update_simple_field(db, 'ENTIDADES', 'alias', json['alias'], 'id', organizacion['id'])
        organizacion['alias'] = json['alias']
    __update_organizacion(db, organizacion, json)
    return organizacion


def __update_organizacion(db, organizacion, json):
    for change in json['data']:
        db_utils.update_simple_field(db, table_name=json['tabla'], field_name=change['field'], value=change['value'],
                                     id_name=json['id'], id_value=organizacion['id'])
        organizacion[change['field']] = change['value']
    return organizacion

@transaction
def delete_organizacion(db, json):
    personajes = db_personajes.get_miembros(db, json['organizacion_id'])
    for personaje in personajes:
        db_utils.update_simple_field(db, 'PERSONAJES', 'organizacion_id', None, 'entidad_id', personaje['id'])
    organizacion = db_organizaciones.get_organizacion(db, json['organizacion_id'])
    db_utils.delete_simple_row(db, 'ORGANIZACIONES', 'entidad_id', organizacion['id'])
    db_utils.delete_simple_row(db, 'ENTIDADES', 'id', organizacion['id'])
    __delete_organizacion(db, organizacion, json)
    return organizacion

def __delete_organizacion(db, organizacion, json):
    db_utils.delete_simple_row(db, table_name=json['tabla'], id_name=json['id'], id_value=organizacion['id'])
    return organizacion
