import streamlit as st
import pandas as pd
from agents.sql_agent import get_query_response
from agents.recommendation_agent import get_recommended_questions
from utils.config import init_langsmith


# Langsmith 설정
init_langsmith()


def render_chat_section():
    st.title("🤖 Northwind Chat")

    # 세션 상태 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "recommended_questions" not in st.session_state:
        st.session_state.recommended_questions = [
            "최근 한 달간 가장 많이 팔린 제품은?",
            "각 직원별 총 판매액은?",
            "가장 많은 주문을 한 고객의 정보는?",
        ]

    # 채팅 기록을 표시할 컨테이너
    chat_container = st.container()

    # 사용자 입력
    with st.form(key="chat_form"):
        col1, col2 = st.columns([9, 1])
        with col1:
            user_input = st.text_input(
                "",
                key="user_input",
                placeholder="예: 고객 중 가장 구매를 많이 한 top 10명과 각각의 구매액은?",
            )
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            submit_button = st.form_submit_button("전송")
        st.markdown("</div>", unsafe_allow_html=True)

    # 추천 질문 버튼
    st.subheader("추천 질문")
    col1, col2, col3 = st.columns(3)
    for i, col in enumerate([col1, col2, col3]):
        with col:
            if i < len(st.session_state.recommended_questions):
                if st.button(st.session_state.recommended_questions[i]):
                    user_input = st.session_state.recommended_questions[i]
                    submit_button = True

    # 사용자 입력 처리
    if submit_button and user_input:
        process_user_input(user_input, chat_container)

    # 채팅 기록 표시
    display_chat_history(chat_container)


def process_user_input(user_input, chat_container):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("응답을 생성 중입니다..."):
        response = get_query_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.session_state.recommended_questions = get_recommended_questions(
        user_input, response
    )


def display_chat_history(chat_container):
    with chat_container:
        for message in st.session_state.messages[-4:]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    display_table_if_applicable(message["content"])


def display_table_if_applicable(content):
    if isinstance(content, str) and "|" in content:
        try:
            df = pd.read_csv(
                pd.compat.StringIO(content), sep="|", skipinitialspace=True
            )
            st.dataframe(df)
        except:
            st.text("결과를 표 형태로 표시할 수 없습니다.")


if __name__ == "__main__":
    render_chat_section()
