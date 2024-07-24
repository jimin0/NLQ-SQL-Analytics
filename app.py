import streamlit as st
from streamlit_option_menu import option_menu

# 페이지 설정
st.set_page_config(layout="wide", page_title="옥돌민님의 대시보드")

# CSS 스타일
st.markdown(
    """
<style>
    header, footer {visibility: hidden;}
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #ff9900;
    }
    .sub-font {
        font-size:16px;
        color: #333;
    }
    .stButton>button {
        background-color: #f0f0f0;
        color: #333;
        border: none;
        border-radius: 20px;
        padding: 5px 10px;
    }
    .send-button {
        background-color: #FFDAB9;
        color: white;
        border: none;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .content-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 10px;
        margin: 10px 0;
    }
    
</style>
""",
    unsafe_allow_html=True,
)

# 사이드바
with st.sidebar:
    st.image("https://placehold.co/100x100.png", width=50)
    selected = option_menu(
        menu_title=None,
        options=["홈", "내 브리핑", "소셜 브리핑", "검색", "리소스"],
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

# 메인 컨텐츠
st.markdown(
    '<p class="big-font">옥돌민님, 안녕하세요. 오늘은 어떤 도움을 드릴까요?</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-font">당신의 관심에 대해 말해주세요. 연구하고, 수집하고, 통찰력을 제공하겠습니다.</p>',
    unsafe_allow_html=True,
)

# 검색 및 질문 섹션
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("", placeholder="메시지를 입력해주세요.")
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

# 메인 대시보드 섹션
st.markdown("## 옥돌민님을 위해 골라봤어요!")
st.markdown("클릭하고 좋아요 하고 북마크 할 수록 선호하는 콘텐츠가 추천될 거에요!")

# 콘텐츠 카드
col1, col2, col3 = st.columns(3)
with col1:
    with st.container():
        st.markdown(
            '<div class="content-card"><h3>콘텐츠 제목 1</h3><p>간단한 설명...</p></div>',
            unsafe_allow_html=True,
        )
with col2:
    with st.container():
        st.markdown(
            '<div class="content-card"><h3>콘텐츠 제목 2</h3><p>간단한 설명...</p></div>',
            unsafe_allow_html=True,
        )
with col3:
    with st.container():
        st.markdown(
            '<div class="content-card"><h3>콘텐츠 제목 3</h3><p>간단한 설명...</p></div>',
            unsafe_allow_html=True,
        )
