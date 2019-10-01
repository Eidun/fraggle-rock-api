from db.impl import db_lugares
from db import transaction
from db import db_utils


@transaction
def get_lugares(db):
    lugares = db_lugares.get_lugares(db)
    return lugares


@transaction
def get_lugar(db, json):
    lugar = db_lugares.get_lugar(db, json['lugar_id'])
    return lugar


@transaction
def create_lugar(db, json):
    lugar = db_lugares.create_lugar(db)
    __update_lugar(db, lugar, json)
    return lugar


@transaction
def update_lugar(db, json):
    lugar = db_lugares.get_lugar(db, json['lugar_id'])
    __update_lugar(db, lugar, json)
    return lugar


def __update_lugar(db, lugar, json):
    for change in json['data']:
        db_utils.update_simple_field(db, table_name=json['tabla'], field_name=change['field'], value=change['value'],
                                     id_name=json['id'], id_value=lugar['id'])
        lugar[change['field']] = change['value']
    return lugar
