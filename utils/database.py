from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase
import os


def get_database():
    db_path = os.getenv("DB_PATH")
    print(db_path)
    if not os.path.exists(db_path):
        raise Exception("데이터베이스 파일이 존재하지 않습니다.")

    db_uri = f"sqlite:///{db_path}"
    engine = create_engine(db_uri)
    return SQLDatabase(engine)
