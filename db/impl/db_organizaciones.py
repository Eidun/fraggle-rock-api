import db.QUERIES as QUERIES


def create_organizacione(db, json):
    db.execute(QUERIES.NEW_ORGANIZACION, (json['alias'],))
    db.execute(QUERIES.SELECT_CREATED_ORGANIZACION)
    organizacion = transform_data(db.fetchone())
    return organizacion


def get_organizacion(db, id_organizacion):
    db.execute(QUERIES.SELECT_ORGANIZACION, (id_organizacion,))
    organizacion_db = db.fetchone()
    organizacion = transform_data(organizacion_db)
    return organizacion


def get_organizaciones(db):
    db.execute(QUERIES.SELECT_ORGANIZACIONES)
    organizaciones_db = db.fetchall()
    organizaciones = []
    for organizacion_db in organizaciones_db:
        organizacion = transform_data(organizacion_db)
        organizaciones.append(organizacion)

    return organizaciones


def transform_data(organizacion_db):
    print(organizacion_db)
    organizacion = {
        'id': organizacion_db[0],
        'numero_miembros': organizacion_db[1],
        'nivel_poder': organizacion_db[2],
        'imagen': organizacion_db[3],
        'lider_id': organizacion_db[4],
        'descripcion': organizacion_db[5],
        'status': organizacion_db[6],
        'alias': organizacion_db[7],

    }
    print(organizacion)
    return organizacion



