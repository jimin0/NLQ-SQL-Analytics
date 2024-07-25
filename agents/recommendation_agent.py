from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from utils.config import MODEL_NAME, OPENAI_API_KEY
from utils.database import get_database

# LLM 초기화
llm = ChatOpenAI(model=MODEL_NAME, temperature=0.7, api_key=OPENAI_API_KEY)

# 데이터베이스 스키마 정보 가져오기
db = get_database()
schema_info = db.get_table_info()

# 프롬프트 템플릿 정의
prompt_template = ChatPromptTemplate.from_template(
    """Northwind 데이터베이스의 스키마 정보:
{schema_info}

이전 질문: {previous_question}
이전 응답: {previous_answer}

위의 대화 맥락과 데이터베이스 스키마를 바탕으로, Northwind 데이터베이스에 관련된 3가지 후속 질문을 생성해주세요. 
질문은 간결하고 구체적이어야 하며, 데이터베이스의 다양한 측면(제품, 고객, 직원, 주문 등)을 다루어야 합니다.
데이터베이스 스키마를 참고하여 실제로 질의 가능한 질문을 만들어주세요.

질문 1:
질문 2:
질문 3:
"""
)

# LLMChain 생성
llm_chain = LLMChain(llm=llm, prompt=prompt_template)


def get_recommended_questions(previous_question, previous_answer):
    # LLM을 사용하여 추천 질문 생성
    response = llm_chain.invoke(
        {
            "schema_info": schema_info,
            "previous_question": previous_question,
            "previous_answer": previous_answer,
        }
    )

    # 응답에서 질문 추출
    generated_questions = response["text"].split("\n")
    # "질문 1:", "질문 2:", "질문 3:" 제거 및 공백 제거
    cleaned_questions = [
        q.split(":", 1)[-1].strip()
        for q in generated_questions
        if q.strip() and ":" in q
    ]

    return cleaned_questions[:3]  # 최대 3개의 질문 반환
