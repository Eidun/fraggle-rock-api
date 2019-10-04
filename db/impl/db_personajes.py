import db.QUERIES as QUERIES


def create_personaje(db, json):
    db.execute(QUERIES.NEW_PERSONAJE, (json['alias'],))
    db.execute(QUERIES.SELECT_CREATED_PERSONAJE)
    personaje = transform_data(db.fetchone())
    return personaje


def get_personaje(db, id_personaje):
    db.execute(QUERIES.SELECT_PERSONAJE, (id_personaje,))
    personaje_db = db.fetchone()
    personaje = transform_data(personaje_db)
    return personaje


def get_personajes(db):
    db.execute(QUERIES.SELECT_PERSONAJES)
    personajes_db = db.fetchall()
    personajes = []
    for personaje_db in personajes_db:
        personaje = transform_data(personaje_db)
        personajes.append(personaje)
    return personajes


def get_miembros(db, organizacion_id):
    db.execute(QUERIES.SELECT_MIEMBROS, (organizacion_id,))
    personajes_db = db.fetchall()
    personajes = []
    for personaje_db in personajes_db:
        personaje = transform_data(personaje_db)
        personajes.append(personaje)

    return personajes


def transform_data(personaje_db):
    personaje = {
        'id': personaje_db[0],
        'organizacion_id': personaje_db[1],
        'residencia_id': personaje_db[2],
        'nombre': personaje_db[3],
        'apellidos': personaje_db[4],
        'rango': personaje_db[5],
        'edad': personaje_db[6],
        'raza': personaje_db[7],
        'descripcion': personaje_db[8],
        'imagen': personaje_db[9],
        'alias': personaje_db[10],
    }
    if len(personaje_db) > 11:
        personaje['alias_organizacion'] = personaje_db[11]
    return personaje
