import streamlit as st
from sidebar import render_sidebar
from main_content import render_main_content

# 페이지 설정
st.set_page_config(layout="wide", page_title="{}님의 대시보드")


# CSS 파일 불러오기
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("styles.css")

# 사이드바 렌더링
render_sidebar()

# 메인 컨텐츠 렌더링
render_main_content()
