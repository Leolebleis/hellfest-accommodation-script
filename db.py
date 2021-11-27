import logging

import psycopg2


logger = logging.getLogger(__name__)

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS hellfest_hebergement_accommodations(accommodation_id serial PRIMARY KEY);
"""


class AccommodationDatabase:
    def __init__(self, host, username, password, port, dbname):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.dbname = dbname
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname,
                )
            except psycopg2.DatabaseError as e:
                logger.error(e)
                raise e

        with self.conn.cursor() as cur:
            cur.execute(CREATE_TABLE_QUERY)

    def insert_rows(self, accommodation_ids: list[str]):
        self.connect()
        with self.conn.cursor() as cur:
            args_str = ",".join(
                f"({accommodation_id})" for accommodation_id in accommodation_ids
            )
            query = f"INSERT INTO hellfest_hebergement_accommodations(accommodation_id) VALUES {args_str}"

            cur.execute(query)
            self.conn.commit()
            cur.close()
            return f"{cur.rowcount} rows affected."

    def select_rows(self, accommodation_id: tuple[str, ...]):
        query = f"SELECT * FROM hellfest_hebergement_accommodations WHERE accommodation_id IN {accommodation_id}"
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = cur.fetchall()
            cur.close()
            return records
