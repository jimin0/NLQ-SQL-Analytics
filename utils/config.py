from dotenv import load_dotenv
import os
from langchain_teddynote import logging

# 환경 변수 로드
load_dotenv()

# 설정 변수
MODEL_NAME = "gpt-4o-mini"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def init_langsmith():
    logging.langsmith("wiset-project")
