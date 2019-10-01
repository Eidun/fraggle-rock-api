import db.QUERIES as QUERIES
from db import transaction


@transaction
def initialize_database(db):
    db.execute(open('db/initialize.sql', 'r').read())


def update_simple_field(db, table_name, field_name, value, id_name, id_value):
    final_query = QUERIES.SIMPLE_FIELD_UPDATE.replace('%TABLE%', table_name) \
        .replace('%FIELD%', field_name).replace('%ID%', id_name)
    db.execute(final_query, (value, id_value))
