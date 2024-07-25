import streamlit as st
from helper_utils import render_content_card
from utils.config import get_username


def render_content_section():
    USER_NAME = get_username()
    # 메인 대시보드 섹션
    st.markdown("## ")
    st.markdown(f"## {USER_NAME}님을 위해 골라봤어요!")
    st.markdown("오늘 회사 공지사항을 확인해보세요.")

    # 콘텐츠 카드
    col1, col2, col3 = st.columns(3)
    with col1:
        render_content_card("콘텐츠 제목 1", "간단한 설명...")
    with col2:
        render_content_card("콘텐츠 제목 2", "간단한 설명...")
    with col3:
        render_content_card("콘텐츠 제목 3", "간단한 설명...")
