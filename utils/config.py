from langchain_teddynote import logging
import streamlit as st
from openai import OpenAI

# 설정 변수
MODEL_NAME = "gpt-4o-mini"


def init_langsmith():
    logging.langsmith("wiset-project")


def get_openai_api_key():
    # 사이드바에서 입력한 OpenAI API Key를 반환합니다.
    return st.session_state.get("chatbot_api_key", "")


def get_username():
    return st.session_state.get("username")


def is_valid_api_key(api_key):
    if not api_key:
        return False
    client = OpenAI(api_key=api_key)
    try:
        client.models.list()
        return True
    except:
        return False
