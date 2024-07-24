import streamlit as st
from helper_utils import render_content_card


def render_content_section():
    # 메인 대시보드 섹션
    st.markdown("## 옥돌민님을 위해 골라봤어요!")
    st.markdown("클릭하고 좋아요 하고 북마크 할 수록 선호하는 콘텐츠가 추천될 거에요!")

    # 콘텐츠 카드
    col1, col2, col3 = st.columns(3)
    with col1:
        render_content_card("콘텐츠 제목 1", "간단한 설명...")
    with col2:
        render_content_card("콘텐츠 제목 2", "간단한 설명...")
    with col3:
        render_content_card("콘텐츠 제목 3", "간단한 설명...")
