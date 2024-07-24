import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():
    with st.sidebar:
        st.image("https://placehold.co/100x100.png", width=50)
        selected = option_menu(
            menu_title=None,
            options=["홈", "내 브리핑", "마이페이지", "직원", "물류"],
            icons=["house", "person", "people", "search", "book"],
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
