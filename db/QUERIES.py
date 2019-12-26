# ======================================================================================================================
#   Create tables
# ======================================================================================================================
CREATE_ENTIDADES_TABLE = "CREATE TABLE ENTIDADES (id serial PRIMARY KEY, clase text, alias text)"

CREATE_LUGARES_TABLE = "CREATE TABLE LUGARES (id serial PRIMARY KEY, nombre text, sector text, sistema text, " \
                       "nivel_tecnologico text, nivel_seguridad text, poblacion number, dominado_por integer, " \
                       "FOREIGN KEY (dominado_por) REFERENCES ENTIDADES(id), descripcion text, clase text)"

CREATE_ORGANIZACIONES_TABLE = "CREATE TABLE ORGANIZACIONES (id serial PRIMARY KEY,  numero_miembros number, " \
                              "nivel_poder text, lider_id integer, status text, descripcion text)"

CREATE_PERSONAJES_TABLE = "CREATE TABLE PERSONAJES (id serial PRIMARY KEY, organizacion_id integer, " \
                          "residencia_id integer, nombre text, apellidos text, rango text, edad number, raza text, " \
                          "FOREIGN KEY (residencia_id) REFERENCES LUGARES(id), descripcion text)"

ADD_LIDER = "ALTER TABLE ORGANIZACIONES ADD CONSTRAINT fk_lider_id FOREIGN KEY (lider_id) REFERENCES PERSONAJES(id)"
ADD_MEMBRESIA = "ALTER TABLE PERSONAJES ADD CONSTRAINT fk_organizacion_id FOREIGN KEY (organizacion_id) " \
                "REFERENCES PERSONAJES(id)"

CREATE_NAVES_TABLE = "CREATE TABLE NAVES (id serial PRIMARY KEY, comandante_id integer REFERENCES PERSONAJES, " \
                     "organizacion_id integer, REFERENCES ORGANIZACIONES, nombre text, modelo text, " \
                     "caracteristicas text, FOREIGN KEY (comandante_id) REFERENCES PERSONAJES(id), " \
                     "FOREIGN KEY (organizacion_id) REFERENCES ORGANIZACIONES(id), clase text), descripcion text)"

CREATE_PLANETAS_TABLE = "CREATE TABLE PLANETAS (lugar_id integer, temperatura text, diametro text, tipo text, " \
                        "atmosfera_respirable boolean, recursos text, FOREIGN KEY (lugar_id) REFERENCES LUGARES(id))"

CREATE_CIUDADES_TABLE = "CREATE TABLE CIUDADES (lugar_id integer, planeta_id integer, " \
                        "FOREIGN KEY (lugar_id) REFERENCES LUGARES(id), " \
                        "FOREIGN KEY (planeta_id) REFERENCES PLANETAS(id))"

CREATE_ESTACIONES_ESPACIALES_TABLE = "CREATE TABLE ESTACIONES_ESPACIALES (lugar_id interger, nave_id integer," \
                                     "FOREIGN KEY (lugar_id) REFERENCES LUGARES(id), " \
                                     "FOREIGN KEY (nave_id) REFERENCES NAVES(id))"

CREATE_CRIMINALES_TABLE = "CREATE TABLE CRIMINALES (personaje_id integer, peligrosidad text, recompensa text, " \
                          "FOREIGN KEY (personaje_id) REFERENCES PERSONAJES(id))"

CREATE_RUTAS_TABLE = "CREATE TABLE RUTAS (lugar1 integer, lugar2 integer, duracion text, nivel_peligro text, " \
                     "tipo_peligro text, FOREIGN KEY (lugar1) REFERENCES LUGARES(id)," \
                     "FOREIGN KEY (lugar2) REFERENCES LUGARES(id), descripcion text)"

# ======================================================================================================================
#   Inserts
# ======================================================================================================================
NEW_PERSONAJE = "INSERT INTO ENTIDADES (clase, alias) VALUES ('Personaje', %s);" \
                "INSERT INTO PERSONAJES (entidad_id)" \
                "SELECT MAX(id) FROM entidades;"

NEW_ORGANIZACION = "INSERT INTO ENTIDADES (clase, alias) VALUES ('Organización', %s);" \
                   "INSERT INTO ORGANIZACIONES (entidad_id)" \
                   "SELECT MAX(id) FROM entidades;"

NEW_NAVE = "INSERT INTO NAVES DEFAULT VALUES;"

NEW_LUGAR = "INSERT INTO LUGARES DEFAULT VALUES;"

NEW_PLANETA = "INSERT INTO LUGARES (clase) VALUES ('Planeta');" \
              "INSERT INTO PLANETAS (lugar_id)" \
              "SELECT MAX(id) FROM LUGARES;"

NEW_CIUDAD = "INSERT INTO LUGARES (clase) VALUES ('Ciudad');" \
             "INSERT INTO CIUDADES (lugar_id)" \
             "SELECT MAX(id) FROM LUGARES;" \
             "SELECT * FROM CIUDADES;"

NEW_ESTACION_ESPACIAL = "INSERT INTO LUGARES (clase) VALUES ('Estación espacial');" \
                        "INSERT INTO NAVES (clase) VALUES ('Estación espacial');" \
                        "INSERT INTO ESTACIONES_ESPACIALES (lugar_id, nave_id)" \
                        "SELECT MAX(L.id), MAX(N.id) FROM LUGARES L, NAVES N;"
# ======================================================================================================================
#   Queries
# ======================================================================================================================

SELECT_LUGARES = "SELECT L.* FROM LUGARES L"
SELECT_CREATED_LUGAR = "SELECT * FROM LUGARES WHERE id=(SELECT MAX(id) FROM LUGARES)"
SELECT_LUGAR = "SELECT * FROM LUGARES WHERE ID=%s"

SELECT_PLANETAS = "SELECT L.*, P.* FROM LUGARES L, PLANETAS P WHERE L.id=P.lugar_id"
SELECT_CREATED_PLANETA = "SELECT L.*, P.* FROM LUGARES L, PLANETAS P WHERE L.id=P.lugar_id AND L.id=(SELECT MAX(L2.id) FROM LUGARES L2)"
SELECT_PLANETA = "SELECT L.*, P.* FROM LUGARES L, PLANETAS P WHERE L.id=P.lugar_id AND L.id=%s"

SELECT_CIUDADES = "SELECT L.*, C.* FROM LUGARES L, CIUDADES C WHERE L.id=C.lugar_id"
SELECT_CREATED_CIUDAD = "SELECT L.*, P.* FROM LUGARES L, CIUDADES C WHERE L.id=C.lugar_id AND L.id=(SELECT MAX(L2.id) FROM LUGARES L2)"
SELECT_CIUDAD = "SELECT L.*, P.* FROM LUGARES L, CIUDADES C WHERE L.id=C.lugar_id AND L.id=%s"

SELECT_NAVES = "SELECT N.*, (SELECT E.alias FROM ENTIDADES E WHERE E.id=N.comandante_id) AS alias_comandante FROM NAVES N"
SELECT_CREATED_NAVE = "SELECT * FROM NAVES WHERE id=(SELECT MAX(id) FROM NAVES)"
SELECT_NAVE = "SELECT * FROM NAVES WHERE ID=%s"

SELECT_ENTIDADES = "SELECT * FROM ENTIDADES"

SELECT_PERSONAJES = "SELECT P.*, E.alias, (SELECT E2.alias FROM ENTIDADES E2 WHERE P.organizacion_id=E2.ID) as alias_organizacion FROM PERSONAJES P, ENTIDADES E WHERE P.entidad_id=E.id"
SELECT_MIEMBROS = "SELECT P.*, E.alias, (SELECT E2.alias FROM ENTIDADES E2 WHERE P.organizacion_id=E2.ID) as alias_organizacion FROM PERSONAJES P, ENTIDADES E WHERE P.entidad_id=E.id AND P.organizacion_id=%s"
SELECT_CREATED_PERSONAJE = "SELECT P.*, E.alias FROM PERSONAJES P, ENTIDADES E WHERE entidad_id=(SELECT MAX(entidad_id) FROM PERSONAJES) AND P.entidad_id=E.id"
SELECT_PERSONAJE = "SELECT P.*, E.alias FROM PERSONAJES P, ENTIDADES E WHERE entidad_id=%s AND P.entidad_id=E.id"

SELECT_ORGANIZACIONES = "SELECT O.*, E.alias FROM ORGANIZACIONES O, ENTIDADES E WHERE O.entidad_id=E.id"
SELECT_ORGANIZACION = "SELECT O.*, E.alias FROM ORGANIZACIONES O, ENTIDADES E WHERE entidad_id=%s AND O.entidad_id=E.id"
SELECT_CREATED_ORGANIZACION = "SELECT O.*, E.alias FROM ORGANIZACIONES O, ENTIDADES E WHERE entidad_id=(SELECT MAX(entidad_id) FROM ORGANIZACIONES) AND O.entidad_id=E.id"


# ======================================================================================================================
#   Updates
# ======================================================================================================================

SIMPLE_FIELD_UPDATE = "UPDATE %TABLE% SET %FIELD%=%s WHERE %ID%=%s"

# ======================================================================================================================
#   Deletes
# ======================================================================================================================

SIMPLE_ROW_DELETE = "DELETE FROM %TABLE% WHERE %ID%=%s "
