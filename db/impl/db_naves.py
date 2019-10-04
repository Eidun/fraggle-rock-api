import db.QUERIES as QUERIES


def create_nave(db):
    db.execute(QUERIES.NEW_NAVE)
    db.execute(QUERIES.SELECT_CREATED_NAVE)
    nave = transform_data(db.fetchone())
    return nave


def get_nave(db, id_nave):
    db.execute(QUERIES.SELECT_NAVE, (id_nave,))
    nave_db = db.fetchone()
    nave = transform_data(nave_db)
    return nave


def get_naves(db):
    db.execute(QUERIES.SELECT_NAVES)
    naves_db = db.fetchall()
    naves = []
    for nave_db in naves_db:
        nave = transform_data(nave_db)
        naves.append(nave)

    return naves


def transform_data(nave_db):
    nave = {
        'id': nave_db[0],
        'comandante_id': nave_db[1],
        'organizacion_id': nave_db[2],
        'nombre': nave_db[3],
        'modelo': nave_db[4],
        'descripcion': nave_db[5],
        'imagen': nave_db[6],
        'clase': nave_db[7],
    }
    if len(nave_db) > 8:
        nave['alias_comandante'] = nave_db[8]

    return nave



