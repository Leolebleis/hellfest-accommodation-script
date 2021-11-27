import os

from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

config = {
    "host": DATABASE_URL,
    "username": DATABASE_USERNAME,
    "password": DATABASE_PASSWORD,
    "port": "5432",
    "dbname": DATABASE_NAME
}
