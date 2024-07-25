from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase
from config import DB_URI


def get_database():
    engine = create_engine(DB_URI)
    db = SQLDatabase(engine)
    return db
