import streamlit as st
from chat import render_chat_section
from content_card import render_content_section


def render_main_content():
    st.markdown(
        '<p class="big-font">옥돌민님, 안녕하세요. 오늘은 어떤 도움을 드릴까요?</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="sub-font">당신의 관심에 대해 말해주세요. 연구하고, 수집하고, 통찰력을 제공하겠습니다.</p>',
        unsafe_allow_html=True,
    )

    render_chat_section()
    render_content_section()
