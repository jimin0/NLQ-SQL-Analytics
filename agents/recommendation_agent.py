from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from utils.config import MODEL_NAME, get_openai_api_key
from utils.database import get_database


def create_llm():
    openai_api_key = get_openai_api_key()
    if not openai_api_key:
        raise ValueError("OpenAI API Key가 제공되지 않았습니다.")
    return ChatOpenAI(model=MODEL_NAME, temperature=0.7, api_key=openai_api_key)


db = get_database()
schema_info = db.get_table_info()

prompt_template = ChatPromptTemplate.from_template(
    """Northwind 데이터베이스의 스키마 정보:
{schema_info}

대화 히스토리:
{chat_history}

마지막 질문: {last_question}
마지막 응답: {last_answer}

위의 대화 맥락과 데이터베이스 스키마를 바탕으로, 다음 조건을 만족하는 3가지 후속 질문을 생성해주세요:
1. 질문은 간결하고 구체적이어야 합니다.
2. 이전 대화 내용과 연관성이 있어야 합니다.
3. 만약 이전 대화가 Northwind 데이터베이스와 관련된 내용이라면:
   a. 데이터베이스의 다양한 측면(제품, 고객, 직원, 주문 등)을 다루어야 합니다.
   b. 데이터베이스 스키마를 참고하여 실제로 질의 가능한 질문이어야 합니다.
4. 만약 이전 대화가 일반적인 주제였다면:
   a. 해당 주제와 관련된 추가 질문을 생성하세요.
   b. 필요하다면 대화를 자연스럽게 Northwind 회사나 비즈니스 관련 주제로 전환할 수 있는 질문을 포함하세요.
5. 대화의 흐름을 자연스럽게 유지하면서 사용자의 관심사를 더 깊이 탐구할 수 있는 질문을 만드세요.

질문 1:
질문 2:
질문 3:
"""
)


def get_recommended_questions(last_question, last_answer, chat_history):
    llm = create_llm()
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)

    # LLM을 사용하여 추천 질문 생성
    response = llm_chain.invoke(
        {
            "schema_info": schema_info,
            "chat_history": chat_history,
            "last_question": last_question,
            "last_answer": last_answer,
        }
    )

    # 응답에서 질문 추출
    generated_questions = response["text"].split("\n")
    cleaned_questions = [
        q.split(":", 1)[-1].strip()
        for q in generated_questions
        if q.strip() and ":" in q
    ]

    return cleaned_questions[:3]  # 최대 3개의 질문 반환
