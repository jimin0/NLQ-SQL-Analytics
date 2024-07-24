import streamlit as st

def render_content_card(title, description):
    with st.container():
        st.markdown(
            f'<div class="content-card"><h3>{title}</h3><p>{description}</p></div>',
            unsafe_allow_html=True,
        )
