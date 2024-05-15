from sqlalchemy import create_engine
from models.good import Base
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker

load_dotenv()  # загрузить переменные окружения из файла .env

# использовать переменные окружения для настройки подключения к базе данных
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")

ur_p = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(ur_p, echo=True)

def create_db_connection():

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()