import streamlit as st
from chat import render_chat_section
from content_card import render_content_section
from utils.config import get_username


def render_main_content():
    USER_NAME = get_username()
    st.markdown(
        f'<p class="big-font">안녕하세요, {USER_NAME}님. 오늘은 어떤 도움을 드릴까요?</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-font"> 고객에 대한 정보, 화사의 업무, 모든 걸 도와드립니다.</p>',
        unsafe_allow_html=True,
    )

    render_chat_section()
    render_content_section()
