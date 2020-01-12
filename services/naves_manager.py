from db.impl import db_naves
from db import transaction
from db import db_utils


@transaction
def get_naves(db):
    naves = db_naves.get_naves(db)
    return naves


@transaction
def get_nave(db, json):
    nave = db_naves.get_nave(db, json['nave_id'])
    nave['tripulantes'] = db_naves.get_tripulantes(db, json['nave_id'])
    return nave


@transaction
def create_nave(db, json):
    nave = db_naves.create_nave(db)
    __update_nave(db, nave, json)
    return nave


@transaction
def update_nave(db, json):
    nave = db_naves.get_nave(db, json['nave_id'])
    __update_nave(db, nave, json)
    return nave


def __update_nave(db, nave, json):
    for change in json['data']:
        db_utils.update_simple_field(db, table_name=json['tabla'], field_name=change['field'], value=change['value'],
                                     id_name=json['id'], id_value=nave['id'])
        nave[change['field']] = change['value']
    return nave
