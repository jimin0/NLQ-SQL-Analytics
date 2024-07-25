import streamlit as st
from sidebar import render_sidebar
from main_content import render_main_content
from utils.config import init_langsmith, get_openai_api_key, get_username
from dashboard import render_dashboard
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 페이지 설정
st.set_page_config(layout="wide", page_title="대시보드")


# CSS 파일 불러오기
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("styles.css")

# 사이드바 렌더링
selected = render_sidebar()

# 선택된 메뉴에 따라 콘텐츠 렌더링
if selected == "홈":
    render_main_content()
elif selected == "대시보드":  # "현재 대시보드"를 "대시보드"로 변경
    render_dashboard()

# Langsmith 초기화
init_langsmith()

# # 입력한 OpenAI API Key와 Username 출력 - 디버깅
# st.write(f"API Key: {get_openai_api_key()}")
# st.write(f"Username: {get_username()}")
