from dotenv import load_dotenv
import os
from langchain_teddynote import logging

# 환경 변수 로드
load_dotenv()

# Langsmith 설정
logging.langsmith("wiset-project")

# 데이터베이스 설정
DB_PATH = os.getenv("DB_PATH")
DB_URI = f"sqlite:///{DB_PATH}"

# OpenAI API 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 모델
MODEL_NAME = "gpt-4o-mini"
