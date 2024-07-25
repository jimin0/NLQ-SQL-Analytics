from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from utils.config import MODEL_NAME, OPENAI_API_KEY
from utils.database import get_database

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
