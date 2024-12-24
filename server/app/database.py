import os
from sqlmodel import create_engine, Session, SQLModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
engine = create_engine(f"sqlite:///{BASE_DIR}/sqlite3.db", echo=True)
SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
