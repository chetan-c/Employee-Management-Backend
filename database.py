import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


database_url = URL.create(
    "postgresql+psycopg",
    username=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    host=os.getenv("DATABASE_HOST"),
    port=int(os.getenv("DATABASE_PORT", "5432")),
    database=os.getenv("DATABASE_NAME"),
)


engine = create_engine(database_url)


SessionLocal = sessionmaker(bind=engine)