import streamlit as st


def render_chat_section():
    # 검색 및 질문 섹션
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("", placeholder="예: 오늘 구입한 제품 수량은?")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        query_button = st.button("Submit", key="query_button")
    st.markdown("</div>", unsafe_allow_html=True)
    # 질문 제안
    st.button("RAG은 어떻게 구현해야 할까요?")
    st.button("RAG와 LLM 푸시를 위한 안전한 시스템은 어떤 특징이 있나요?")
    st.button(
        "AI 포럼, AIM 및 NVIDIA가 제시한 RAG 모델 최적화 마스터 클래스에는 어떤 내용이 포함되어 있나요?"
    )
