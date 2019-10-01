import psycopg2
from db.db_config import config


def __create_connection():
    conn = psycopg2.connect(
        database=config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )
    return conn


def transaction(f):
    def do_transaction(*args, **kwargs):
        # or use a pool, or a factory function...
        conn = __create_connection()
        db = conn.cursor()
        try:
            rv = f(db, *args, **kwargs)
        except Exception as e:
            conn.rollback()
            raise
        else:
            conn.commit()
            db.close()
        finally:
            conn.close()

        return rv

    return do_transaction
