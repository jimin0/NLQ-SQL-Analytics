from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()


def get_database():
    db_path = os.getenv("DB_PATH")
    print(db_path)
    if not os.path.exists(db_path):
        raise Exception("데이터베이스 파일이 존재하지 않습니다.")

    db_uri = f"sqlite:///{db_path}"
    engine = create_engine(db_uri)
    return SQLDatabase(engine)

def get_database2():
    db_path = os.getenv("DB_PATH")
    if db_path is None:
        raise ValueError("환경 변수 'DB_PATH'가 설정되지 않았습니다.")
    if not os.path.exists(db_path):
        raise Exception("데이터베이스 파일이 존재하지 않습니다.")
    
    db_uri = f"sqlite:///{db_path}"
    return create_engine(db_uri)