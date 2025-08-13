import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="과학 선택과목 홍보 ✨", page_icon="🧪", layout="wide")

# 간단한 CSS 꾸미기
st.markdown("""
<style>
:root {--bg: #0b1020; --card: #11172a; --text: #e8ebff; --muted: #9fb0ff; --accent: linear-gradient(135deg,#7c4dff 0%, #00e5ff 100%);}
section.main > div {background: radial-gradient(1200px 500px at 10% 0%, #0f1731 0%, #0b1020 30%, #0b1020 100%) !important;}
html, body, [class*="css" ] { color: var(--text) !important; }
.card {background: rgba(17,23,42,.75); border: 1px solid rgba(255,255,255,.07); padding: 20px; border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.25);} 
.gtitle {font-weight:800; font-size:2.2rem; background:var(--accent); -webkit-background-clip:text; background-clip:text; color:transparent;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🎓 과학 선택 가이드")
nav = st.sidebar.radio("메뉴", ["홈", "MBTI 추천", "물리학", "화학", "생명과학", "지구과학"])

def subject_card(title, desc):
    st.markdown(f"<div class='card'><h3 class='gtitle'>{title}</h3><p>{desc}</p></div>", unsafe_allow_html=True)

# MBTI 추천 로직
mbti_map = {
    "INTJ": "물리학",
    "INTP": "물리학",
    "ENTJ": "물리학",
    "ENTP": "물리학",
    "INFJ": "생명과학",
    "INFP": "생명과학",
    "ENFJ": "생명과학",
    "ENFP": "생명과학",
    "ISTJ": "화학",
    "ISFJ": "화학",
    "ESTJ": "화학",
    "ESFJ": "화학",
    "ISTP": "지구과학",
    "ISFP": "지구과학",
    "ESTP": "지구과학",
    "ESFP": "지구과학",
}

if nav == "홈":
    st.markdown(f"<div class='card'><h1 class='gtitle'>과학 선택과목 로드맵 ✨</h1><p>네 과목을 한 곳에서 비교하고 추천까지!</p></div>", unsafe_allow_html=True)

if nav == "MBTI 추천":
    st.markdown("<h2 class='gtitle'>MBTI로 과목 추천 🎯</h2>", unsafe_allow_html=True)
    mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)").upper()
    if mbti in mbti_map:
        subject = mbti_map[mbti]
        st.success(f"추천 과목은 **{subject}** 입니다!")
        if subject == "물리학":
            subject_card("물리학 ⚛️", "힘·운동·에너지·전자기·파동·우주까지! 세상의 원리를 수식으로 해석하는 과목.")
        elif subject == "화학":
            subject_card("화학 🧪", "원자에서 신소재까지! 물질의 구조와 변화, 반응을 탐구하는 실험 천국.")
        elif subject == "생명과학":
            subject_card("생명과학 🧬", "세포에서 생태계까지! 생명의 정보와 시스템을 파고드는 여정.")
        elif subject == "지구과학":
            subject_card("지구과학 🌍", "지권·대기·해양·우주를 데이터로 읽는 과목.")
    elif mbti != "":
        st.error("올바른 MBTI 4글자를 입력하세요.")

if nav == "물리학":
    subject_card("물리학 ⚛️", "힘·운동·에너지·전자기·파동·우주까지! 세상의 원리를 수식으로 해석하는 과목.")
if nav == "화학":
    subject_card("화학 🧪", "원자에서 신소재까지! 물질의 구조와 변화, 반응을 탐구하는 실험 천국.")
if nav == "생명과학":
    subject_card("생명과학 🧬", "세포에서 생태계까지! 생명의 정보와 시스템을 파고드는 여정.")
if nav == "지구과학":
    subject_card("지구과학 🌍", "지권·대기·해양·우주를 데이터로 읽는 과목.")
