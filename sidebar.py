import streamlit as st
from streamlit_option_menu import option_menu
from utils.config import is_valid_api_key, get_openai_api_key


def render_sidebar():
    with st.sidebar:
        st.image("https://placehold.co/100x100.png", width=50)
        selected = option_menu(
            menu_title=None,
            options=["홈", "대시보드"],
            icons=["house", "bi bi-file-bar-graph"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#f0f0f0"},
                "icon": {"color": "black", "font-size": "18px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#ff9900"},
            },
        )
        st.session_state.selected_menu = selected

        st.markdown("---")

        # Your name:
        myname = st.text_input("name", key="username", on_change=st.experimental_rerun)

        # 사이드바에 OpenAI API 키 입력 필드 생성:
        openai_api_key = st.text_input(
            "OpenAI API Key",
            key="chatbot_api_key",
            type="password",
            on_change=st.experimental_rerun,
        )
        # API 키 유효성 확인 및 메시지 표시
        if openai_api_key:
            if is_valid_api_key(openai_api_key):
                st.markdown(
                    '<p style="color:green;">API 키가 유효합니다.</p>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<p style="color:red;">API 키가 유효하지 않습니다.</p>',
                    unsafe_allow_html=True,
                )

        st.markdown("---")

        clear_btn = st.button("🗑️Clear Chat")

        # 초기화 버튼이 눌리면...
        if clear_btn:
            st.session_state["messages"] = []
            st.experimental_rerun()

    return selected
