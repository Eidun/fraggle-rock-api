DROP TABLE IF EXISTS ENTIDADES CASCADE;
DROP TABLE IF EXISTS LUGARES CASCADE;
DROP TABLE IF EXISTS ORGANIZACIONES CASCADE;
DROP TABLE IF EXISTS PERSONAJES CASCADE;
DROP TABLE IF EXISTS NAVES CASCADE;
DROP TABLE IF EXISTS TRIPULA CASCADE;
DROP TABLE IF EXISTS PLANETAS CASCADE;
DROP TABLE IF EXISTS CIUDADES CASCADE;
DROP TABLE IF EXISTS ESTACIONES_ESPACIALES CASCADE;
DROP TABLE IF EXISTS CRIMINALES CASCADE;
DROP TABLE IF EXISTS RUTAS CASCADE;

CREATE TABLE ENTIDADES (id serial PRIMARY KEY, clase text, alias text);

CREATE TABLE LUGARES (id serial PRIMARY KEY, nombre text, sector text, sistema text, imagen text,
					  nivel_tecnologico text, nivel_seguridad text, poblacion text, descripcion text,
					  dominado_por integer, FOREIGN KEY (dominado_por) REFERENCES ENTIDADES(id), clase text);

CREATE TABLE ORGANIZACIONES (entidad_id integer PRIMARY KEY, numero_miembros text, nivel_poder text,  imagen text,
                        lider_id integer, descripcion text, status text, FOREIGN KEY (entidad_id) REFERENCES ENTIDADES(id));

CREATE TABLE PERSONAJES (entidad_id integer PRIMARY KEY, organizacion_id integer, residencia_id integer, nombre text,
						 apellidos text, rango text, edad text, raza text, descripcion text, imagen text,
						 FOREIGN KEY (residencia_id) REFERENCES LUGARES(id),
						 FOREIGN KEY (entidad_id) REFERENCES ENTIDADES(id));

ALTER TABLE ORGANIZACIONES ADD CONSTRAINT fk_lider_id FOREIGN KEY (lider_id) REFERENCES PERSONAJES(entidad_id);
ALTER TABLE PERSONAJES ADD CONSTRAINT fk_organizacion_id FOREIGN KEY (organizacion_id) REFERENCES ORGANIZACIONES(entidad_id);

CREATE TABLE NAVES (id serial PRIMARY KEY, comandante_id integer, organizacion_id integer,
					nombre text, modelo text, descripcion text, imagen text,
					FOREIGN KEY (comandante_id) REFERENCES PERSONAJES(entidad_id),
					FOREIGN KEY (organizacion_id) REFERENCES ORGANIZACIONES(entidad_id), clase text);

CREATE TABLE TRIPULA (nave_id integer, personaje_id integer, cargo text, FOREIGN KEY (nave_id) REFERENCES NAVES(id),
FOREIGN KEY (personaje_id) REFERENCES PERSONAJES(entidad_id));

CREATE TABLE PLANETAS (lugar_id integer UNIQUE, temperatura text, diametro text, tipo text, atmosfera_respirable boolean,
					   recursos text, FOREIGN KEY (lugar_id) REFERENCES LUGARES(id));

CREATE TABLE CIUDADES (lugar_id integer UNIQUE, planeta_id integer,
					   FOREIGN KEY (lugar_id) REFERENCES LUGARES(id),
					   FOREIGN KEY (planeta_id) REFERENCES PLANETAS(lugar_id));

CREATE TABLE ESTACIONES_ESPACIALES (lugar_id integer, nave_id integer,
									FOREIGN KEY (lugar_id) REFERENCES LUGARES(id),
									FOREIGN KEY (nave_id) REFERENCES NAVES(id));

CREATE TABLE CRIMINALES (personaje_id integer, peligrosidad text, recompensa text,
						 FOREIGN KEY (personaje_id) REFERENCES PERSONAJES(entidad_id));

CREATE TABLE RUTAS (lugar1 integer, lugar2 integer, duracion text, nivel_peligro text, tipo_peligro text,
					FOREIGN KEY (lugar1) REFERENCES LUGARES(id),
					FOREIGN KEY (lugar2) REFERENCES LUGARES(id));
