from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from utils.config import MODEL_NAME, get_openai_api_key
from utils.database import get_database
import streamlit as st

# 데이터베이스 연결
db = get_database()


def create_llm():
    openai_api_key = get_openai_api_key()
    if not openai_api_key:
        raise ValueError("OpenAI API Key가 제공되지 않았습니다.")
    return ChatOpenAI(
        model=MODEL_NAME, temperature=0, streaming=True, api_key=openai_api_key
    )


from utils.config import get_openai_api_key, is_valid_api_key


def get_query_response(query):
    api_key = get_openai_api_key()
    if not api_key:
        raise ValueError("OpenAI API 키가 제공되지 않았습니다.")
    if not is_valid_api_key(api_key):
        raise ValueError("유효하지 않은 OpenAI API 키입니다.")

    llm = create_llm()
    agent_executor = create_sql_agent(
        llm, db=db, agent_type="openai-tools", verbose=True
    )
    try:
        response = agent_executor.invoke(query)["output"]
        print(response)
        return response
    except Exception as e:
        print(f"오류 상세 정보: {str(e)}")
        return None
