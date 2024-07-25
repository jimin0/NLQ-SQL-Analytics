import streamlit as st
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
import pandas as pd
from config import MODEL_NAME, OPENAI_API_KEY
from database import get_database
from langchain_teddynote import logging

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
    st.subheader("데이터베이스 질의")
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input(
            "",
            placeholder="예: 고객 중 가장 구매를 많이 한 top 10명과 각각의 구매액은?",
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        query_button = st.button("질문하기", key="query_button")
    st.markdown("</div>", unsafe_allow_html=True)

    if query_button:
        if user_input:
            with st.spinner("응답을 생성 중입니다..."):
                response = get_query_response(user_input)
                st.write(response)

                # 결과가 테이블 형태라면 DataFrame으로 변환하여 표시
                if isinstance(response, str) and response.strip().startswith("|"):
                    try:
                        df = pd.read_csv(
                            pd.compat.StringIO(response), sep="|", skipinitialspace=True
                        )
                        st.dataframe(df)
                    except:
                        st.text("결과를 표 형태로 표시할 수 없습니다.")
        else:
            st.warning("질문을 입력해주세요.")

    # 추천 질문
    st.subheader("추천 질문")
    if st.button("최근 한 달간 가장 많이 팔린 제품은?"):
        render_chat_section.query = "최근 한 달간 가장 많이 팔린 제품은?"
        st.experimental_rerun()
    if st.button("각 직원별 총 판매액은?"):
        render_chat_section.query = "각 직원별 총 판매액은?"
        st.experimental_rerun()
    if st.button("가장 많은 주문을 한 고객의 정보는?"):
        render_chat_section.query = "가장 많은 주문을 한 고객의 정보는?"
        st.experimental_rerun()

    # 이전 질문이 있다면 자동으로 입력
    if hasattr(render_chat_section, "query"):
        user_input = render_chat_section.query
        del render_chat_section.query
