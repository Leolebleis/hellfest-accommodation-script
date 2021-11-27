import os

from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_SSLMODE = os.getenv("DATABASE_SSLMODE")

config = {
    "url": DATABASE_URL,
    "sslmode": DATABASE_SSLMODE
}
