from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings


def get_database_url():
    if settings.database_url:
        return settings.database_url
    else:
        return "sqlite:///database.db"


DATABASE_URL = get_database_url()

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args=connect_args
)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
