import db.QUERIES as QUERIES


def get_entidades(db):
    db.execute(QUERIES.SELECT_ENTIDADES)
    entidades_db = db.fetchall()
    entidades = []
    for entidad_db in entidades_db:
        entidad = transform_data(entidad_db)
        entidades.append(entidad)

    return entidades


def transform_data(entidad_db):
    entidad = {
        'id': entidad_db[0],
        'clase': entidad_db[1],
        'alias': entidad_db[2],
    }
    return entidad
