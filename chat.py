import streamlit as st
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
import pandas as pd
from config import MODEL_NAME, OPENAI_API_KEY
from database import get_database
from langchain_teddynote import logging
from recommendation import get_recommended_questions

# Langsmith 설정
logging.langsmith("wiset-project")

# 데이터베이스 연결
db = get_database()

# LLM 생성
llm = ChatOpenAI(
    model=MODEL_NAME, temperature=0, streaming=True, api_key=OPENAI_API_KEY
)

# SQL 에이전트 생성
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=False)


def get_query_response(query):
    try:
        response = agent_executor.invoke(query)["output"]
        return response
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"


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
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     if st.button("최근 한 달간 가장 많이 팔린 제품은?"):
    #         user_input = "최근 한 달간 가장 많이 팔린 제품은?"
    #         submit_button = True
    # with col2:
    #     if st.button("각 직원별 총 판매액은?"):
    #         user_input = "각 직원별 총 판매액은?"
    #         submit_button = True
    # with col3:
    #     if st.button("가장 많은 주문을 한 고객의 정보는?"):
    #         user_input = "가장 많은 주문을 한 고객의 정보는?"
    #         submit_button = True

    col1, col2, col3 = st.columns(3)
    for i, col in enumerate([col1, col2, col3]):
        with col:
            if i < len(st.session_state.recommended_questions):
                if st.button(st.session_state.recommended_questions[i]):
                    user_input = st.session_state.recommended_questions[i]
                    submit_button = True

    # 사용자 입력 처리
    if submit_button and user_input:
        # 사용자 메시지 추가
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 챗봇 응답 생성
        with st.spinner("응답을 생성 중입니다..."):
            response = get_query_response(user_input)
            st.session_state.messages.append({"role": "assistant", "content": response})

        # 추천 질문 업데이트
        st.session_state.recommended_questions = get_recommended_questions(
            user_input, response
        )

    # 채팅 기록 표시 (최근 4개 메시지만)
    with chat_container:
        for message in st.session_state.messages[-4:]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

                # 테이블 형태의 응답 처리
                if (
                    message["role"] == "assistant"
                    and isinstance(message["content"], str)
                    and "|" in message["content"]
                ):
                    try:
                        df = pd.read_csv(
                            pd.compat.StringIO(message["content"]),
                            sep="|",
                            skipinitialspace=True,
                        )
                        st.dataframe(df)
                    except:
                        st.text("결과를 표 형태로 표시할 수 없습니다.")

    # 스크롤을 최신 메시지로 이동
    st.query_params.clear()


if __name__ == "__main__":
    render_chat_section()
