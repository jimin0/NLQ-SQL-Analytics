from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from utils.config import MODEL_NAME, get_openai_api_key


def create_router_agent():
    llm = ChatOpenAI(model=MODEL_NAME, temperature=0, api_key=get_openai_api_key())

    prompt = ChatPromptTemplate.from_template(
        "당신은 Northwind라는 회사의 AI 어시스턴트입니다. Northwind는 SQL 데이터베이스를 사용하여 제품, 주문, 고객, 직원 등의 정보를 관리합니다. "
        "사용자의 입력이 Northwind 회사의 SQL 데이터베이스 쿼리와 관련된 질문인지 판단해주세요. "
        "다음과 같은 경우 'SQL'이라고 답변하세요:\n"
        "1. 직접적으로 데이터베이스 정보를 요청하는 경우\n"
        "2. '우리 회사'나 'Northwind'에 대한 데이터 관련 질문\n"
        "3. 제품, 주문, 고객, 직원 등 Northwind 데이터베이스의 엔티티에 대한 정보 요청\n"
        "그 외의 일반적인 대화나 데이터베이스와 관련 없는 질문의 경우 'General'이라고 답변하세요.\n\n"
        "사용자 입력: {user_input}\n"
        "답변: "
    )

    return LLMChain(llm=llm, prompt=prompt)


def route_query(user_input):
    router = create_router_agent()
    response = router.run(user_input)
    return response.strip().lower()
