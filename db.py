import psycopg2


CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS hellfest_hebergement_accommodations(accommodation_id serial PRIMARY KEY);
"""


class AccommodationDatabase:
    def __init__(self, url: str, sslmode: str):
        self.url = url
        self.sslmode = sslmode
        self.conn = None

    def connect(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(self.url, sslmode=self.sslmode)

            except psycopg2.DatabaseError as e:
                print(e)

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
