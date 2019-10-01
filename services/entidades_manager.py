from db.impl import db_entidades
from db import transaction


@transaction
def get_entidades(db):
    entidades = db_entidades.get_entidades(db)
    return entidades
