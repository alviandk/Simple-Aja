import os
import psycopg2

from urllib.parse import urlparse


def get_db_connection():
    database_url = os.environ['DATABASE_URL']
    parsed = urlparse(database_url)
    # postgresql://simple:aja@db:5432/simple_aja_db
    pg_connection_dict = {
        'dbname': database_url.split('/')[-1],
        'user': parsed.username,
        'password': parsed.password,
        'port': parsed.port,
        'host': parsed.hostname
    }

    conn = psycopg2.connect(**pg_connection_dict)
    return conn
