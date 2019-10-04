import db.QUERIES as QUERIES


def create_lugar(db):
    db.execute(QUERIES.NEW_LUGAR)
    db.execute(QUERIES.SELECT_CREATED_LUGAR)
    lugar = transform_data(db.fetchone())
    return lugar


def get_lugar(db, id_lugar):
    db.execute(QUERIES.SELECT_LUGAR, (id_lugar,))
    lugar_db = db.fetchone()
    lugar = transform_data(lugar_db)
    return lugar


def get_lugares(db):
    db.execute(QUERIES.SELECT_LUGARES)
    lugares_db = db.fetchall()
    lugares = []
    for lugar_db in lugares_db:
        lugar = transform_data(lugar_db)
        lugares.append(lugar)

    return lugares


def transform_data(lugar_db):
    print(lugar_db)
    lugar = {
        'id': lugar_db[0],
        'nombre': lugar_db[1],
        'sector': lugar_db[2],
        'sistema': lugar_db[3],
        'imagen': lugar_db[4],
        'nivel_tecnologico': lugar_db[5],
        'nivel_seguridad': lugar_db[6],
        'poblacion': lugar_db[7],
        'descripcion': lugar_db[8],
        'dominado_por': lugar_db[9],
        'clase': lugar_db[10],
    }
    return lugar



