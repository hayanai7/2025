import streamlit as st
import pandas as pd
from datetime import date

# ---------------------------
# 기본 설정
# ---------------------------
st.set_page_config(
    page_title="과학 선택과목 홍보 ✨",
    page_icon="🧪",
    layout="wide",
)

# ---------------------------
# 심플 테마용 CSS (카드/배지/헤더)
# ---------------------------
CUSTOM_CSS = """
<style>
:root {
  --bg: #0b1020;
  --card: #11172a;
  --text: #e8ebff;
  --muted: #9fb0ff;
  --accent: linear-gradient(135deg,#7c4dff 0%, #00e5ff 100%);
}
/* 다크한 그라디언트 배경 */
section.main > div {background: radial-gradient(1200px 500px at 10% 0%, #0f1731 0%, #0b1020 30%, #0b1020 100%) !important;}
/* 본문 글자색 */
html, body, [class*="css" ] { color: var(--text) !important; }
/* 카드 */
.card {background: rgba(17,23,42,.75); border: 1px solid rgba(255,255,255,.07); padding: 20px; border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.25);} 
.card h3 {margin-top: 0;}
/* 배지 */
.badge {display:inline-block; padding:6px 10px; border-radius:999px; border:1px solid rgba(255,255,255,.18); background:rgba(255,255,255,.06); font-size:.85rem; margin-right:6px}
/* 칩 */
.chip {display:inline-block; padding:8px 12px; margin:4px; border-radius:12px; background:rgba(124,77,255,.15); border:1px solid rgba(124,77,255,.35)}
/* 그라디언트 타이틀 */
.gtitle {font-weight:800; font-size:2.2rem; background:var(--accent); -webkit-background-clip:text; background-clip:text; color:transparent;}
.sub {color: var(--muted);}
/* 구분선 */
.hr {height:1px; background:linear-gradient(90deg, transparent, rgba(255,255,255,.25), transparent); margin:14px 0 8px}
/* 이모지 크기 조정 */
.big {font-size: 1.6rem}
/* 표 스타일 개선 */
.dataframe tbody tr:hover { background: rgba(124,77,255,.08) !important; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------
# 사이드바
# ---------------------------
st.sidebar.title("🎓 과학 선택 가이드")
st.sidebar.markdown("**고3 준비는 지금부터!** 🚀\n\n원하는 과목을 눌러 빠르게 살펴보세요 👇")
nav = st.sidebar.radio(
    "섹션 이동",
    ["홈", "물리학", "화학", "생명과학", "지구과학", "비교", "진로", "미니퀴즈", "FAQ"],
    captions=[
        "소개 & 하이라이트",
        "⚛️ 힘·파동·우주",
        "🧪 물질·반응·산업",
        "🧬 세포·유전·생태",
        "🌍 지권·대기·우주",
        "과목 한눈에 비교",
        "대학·직업·스킬맵",
        "가볍게 재미 테스트",
        "자주 묻는 질문",
    ],
    index=0,
)

# 재사용: 과목 카드 컴포넌트

def subject_card(title, emoji, wow, love_points, project_ideas, skills):
    c1, c2 = st.columns([1,1])
    with c1:
        st.markdown(f"<div class='card'><div class='badge'>{emoji} HOT</div>  <h3 class='gtitle'>{title}</h3>\n<p class='sub'>{wow}</p>\n<div class='hr'></div>", unsafe_allow_html=True)
        st.markdown("**이 과목, 이런 학생에게 딱!** ✋")
        st.markdown("\n".join([f"- {p}" for p in love_points]))
        st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
        st.markdown("**프로젝트 아이디어** 💡")
        st.markdown("\n".join([f"- {p}" for p in project_ideas]))
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("**키 스킬** 🧠")
        cols = st.columns(2)
        half = (len(skills)+1)//2
        with cols[0]:
            for s in skills[:half]:
                st.markdown(f"<span class='chip'>✨ {s}</span>", unsafe_allow_html=True)
        with cols[1]:
            for s in skills[half:]:
                st.markdown(f"<span class='chip'>🚀 {s}</span>", unsafe_allow_html=True)
        st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
        st.markdown("**활용 분야** 🌟")
        st.markdown("- 대학 전공 심화, 탐구대회, 동아리 활동, 진로 포트폴리오 업그레이드 ✍️")
        st.markdown("</div>", unsafe_allow_html=True)

# 홈 섹션
if nav == "홈":
    st.markdown("""
    <div class="card">
      <div class="badge">📅 업데이트: {today}</div>
      <h1 class="gtitle">과학 선택과목 로드맵 ✨⚛️🧪🧬🌍</h1>
      <p class="sub">고등학생 여러분, 과학의 세계로 초대합니다!\
      네 과목을 한 곳에서 비교하고, 프로젝트 아이디어와 진로까지 한 번에!</p>
    </div>
    """.format(today=date.today().strftime("%Y-%m-%d")), unsafe_allow_html=True)

    # 하이라이트 배지
    colA, colB, colC, colD = st.columns(4)
    with colA:
        st.markdown("<div class='card'><div class='big'>⚛️</div><b>물리학</b><br><span class='sub'>수학적 사고 · 엔지니어링</span></div>", unsafe_allow_html=True)
    with colB:
        st.markdown("<div class='card'><div class='big'>🧪</div><b>화학</b><br><span class='sub'>물질의 변화 · 실험 설계</span></div>", unsafe_allow_html=True)
    with colC:
        st.markdown("<div class='card'><div class='big'>🧬</div><b>생명과학</b><br><span class='sub'>세포 · 유전 · 의생명</span></div>", unsafe_allow_html=True)
    with colD:
        st.markdown("<div class='card'><div class='big'>🌍</div><b>지구과학</b><br><span class='sub'>지권/대기 · 우주</span></div>", unsafe_allow_html=True)

    st.markdown("<div class='hr'></div>", unsafe_allow_html=True)
    st.markdown("**빠른 비교** 🔍")
    compare = pd.DataFrame([
        ["물리학", "수학 활용도 높음", "엔지니어링/로보틱스", 5, 4, 3],
        ["화학", "실험 빈도 높음", "신소재/제약/반도체", 4, 5, 4],
        ["생명과학", "생명/의학 연계", "의생명/바이오", 3, 4, 5],
        ["지구과학", "데이터/관측", "기상/천문/환경", 3, 3, 4],
    ], columns=["과목", "특징", "진로 키워드", "수학", "실험", "생명 연계"])
    st.dataframe(compare, use_container_width=True)

# 물리학
if nav == "물리학":
    subject_card(
        title="물리학 ⚛️",
        emoji="⚡",
        wow="힘·운동·에너지·전자기·파동·우주까지! 세상의 원리를 수식으로 해석하는 두근두근 과목.",
        love_points=[
            "논리적·수학적 추론을 좋아한다 🧩",
            "엔지니어링/로보틱스에 관심이 많다 🤖",
            "문제 해결을 구조적으로 접근한다 🧠",
        ],
        project_ideas=[
            "DIY 관성 모터·코일건 안전 모델 만들기",
            "도플러 효과로 구급차 소리 분석 앱 만들기",
            "아두이노로 낙하 가속도·충돌 실험 장치",
        ],
        skills=["벡터·미적분 감각", "실험 데이터 피팅", "모델링/시뮬", "전자기 현상 이해", "하드웨어 메이킹", "문제 분해"],
    )

# 화학
if nav == "화학":
    subject_card(
        title="화학 🧪",
        emoji="🔥",
        wow="원자에서 신소재까지! 물질의 구조와 변화, 반응을 탐구하는 실험 천국.",
        love_points=[
            "실험/분석 활동이 즐겁다 🧫",
            "생활 속 화학 현상을 좋아한다 🧴",
            "제약·반도체·신소재가 끌린다 🧯",
        ],
        project_ideas=[
            "친환경 버려지는 껍질로 만든 바이오흡착제 실험",
            "pH 인디케이터로 음료 산도 맵 만들기",
            "전기분해로 수소 생산 효율 비교",
        ],
        skills=["분자구조·결합", "반응속도/평형", "적정/분광분석", "안전한 실험 설계", "데이터 시각화", "화학 공정 사고"],
    )

# 생명과학
if nav == "생명과학":
    subject_card(
        title="생명과학 🧬",
        emoji="🌱",
        wow="세포에서 생태계까지! 생명의 정보와 시스템을 파고드는 흥미진진 여정.",
        love_points=[
            "의학·바이오에 관심이 많다 🏥",
            "생명 현상을 관찰하고 기록하는 걸 좋아한다 🔬",
            "팀 프로젝트·탐구 보고서를 즐긴다 📑",
        ],
        project_ideas=[
            "파리지옥 반응 시간 데이터로 최적 환경 찾기",
            "효소 반응 속도에 온도·pH 영향 모델링",
            "동네 하천 미생물 다양성 메타바코딩 체험",
        ],
        skills=["세포/유전 원리", "실험윤리·안전", "통계적 분석", "생물정보학 기초", "문헌 탐색", "과학 글쓰기"],
    )

# 지구과학
if nav == "지구과학":
    subject_card(
        title="지구과학 🌍",
        emoji="🌋",
        wow="지권·대기·해양·우주를 하나로! 데이터로 지구 시스템을 읽는 과목.",
        love_points=[
            "천문/기상/지질 덕질한다 🔭",
            "사진·지도·그래프 보는 걸 좋아한다 🗺️",
            "환경·기후 문제에 관심이 많다 🌿",
        ],
        project_ideas=[
            "별 관측으로 변광성 주기 분석",
            "미세먼지·기상 데이터로 회귀 모델 만들기",
            "지역 지질 답사·암석 도감 제작",
        ],
        skills=["시계열 데이터", "원격탐사·지도", "통계/회귀 해석", "관측 로그북", "프리젠테이션", "환경 리터러시"],
    )

# 비교 섹션
if nav == "비교":
    st.markdown("<h2 class='gtitle'>과목 한눈에 비교 🔍</h2>", unsafe_allow_html=True)
    df = pd.DataFrame({
        "과목": ["물리학","화학","생명과학","지구과학"],
        "수학 난이도(1~5)": [5,4,3,3],
        "실험 빈도(1~5)": [3,5,4,3],
        "현장/관측(1~5)": [3,3,3,5],
        "진로 연계도(1~5)": [5,5,5,4],
    })
    st.dataframe(df, use_container_width=True)
    st.markdown("**흥미 포인트 점수(예시)** 🎯")
    st.bar_chart(df.set_index("과목"))

# 진로 섹션
if nav == "진로":
    st.markdown("<h2 class='gtitle'>진로 & 스킬맵 🚀</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>📚 추천 전공</h3>
        <p>⚛️ 물리학 → 전기/전자, 기계, 항공우주, 컴퓨터공학, 데이터과학</p>
        <p>🧪 화학 → 화학공학, 신소재, 제약/바이오, 반도체, 환경공학</p>
        <p>🧬 생명과학 → 의생명, 생명공학, 수의·간호·보건, 뇌과학</p>
        <p>🌍 지구과학 → 기상/해양/지질, 환경, 천문/우주과학, 지리정보</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>🧭 역량 로드맵</h3>
        <p>🧠 공통 핵심: <span class='badge'>문제정의</span> <span class='badge'>가설·모델링</span> <span class='badge'>데이터 해석</span> <span class='badge'>커뮤니케이션</span></p>
        <p>💻 도구: <span class='chip'>스프레드시트</span> <span class='chip'>파이썬(선택)</span> <span class='chip'>그래프/시각화</span> <span class='chip'>문헌검색</span></p>
        <p>🏆 활동: 과학탐구보고서, 과제연구, 동아리/탐구대회, UCC 발표</p>
        </div>
        """, unsafe_allow_html=True)

# 미니퀴즈 섹션
if nav == "미니퀴즈":
    st.markdown("<h2 class='gtitle'>미니퀴즈 🎯 오늘 내 적성은?</h2>", unsafe_allow_html=True)
    with st.form("quiz"):
        q1 = st.radio("1) 실험과 관측 중 더 설레는 것은?", ["수식으로 먼저 예측!", "실험 장비 세팅이 좋다", "생물 표본·관찰이 재밌다", "야외 관측/지도 보는 게 좋다"], index=None)
        q2 = st.radio("2) 노트 스타일은?", ["수식+도식 정리", "실험 결과표/그래프", "그림/키워드/정의", "사진/지도/시간표"], index=None)
        q3 = st.radio("3) 진로 키워드가 가장 끌리는 것은?", ["로보틱스/AI/엔지니어링", "제약/반도체/신소재", "의생명/바이오", "기상/천문/환경"], index=None)
        submitted = st.form_submit_button("결과 보기 ✨")
    if submitted:
        score = {"물리학":0, "화학":0, "생명과학":0, "지구과학":0}
        mapping = {
            "수식으로 먼저 예측!": "물리학",
            "실험 장비 세팅이 좋다": "화학",
            "생물 표본·관찰이 재밌다": "생명과학",
            "야외 관측/지도 보는 게 좋다": "지구과학",
            "수식+도식 정리": "물리학",
            "실험 결과표/그래프": "화학",
            "그림/키워드/정의": "생명과학",
            "사진/지도/시간표": "지구과학",
            "로보틱스/AI/엔지니어링": "물리학",
            "제약/반도체/신소재": "화학",
            "의생명/바이오": "생명과학",
            "기상/천문/환경": "지구과학",
        }
        for ans in [q1, q2, q3]:
            if ans: score[mapping[ans]] += 1
        best = max(score, key=score.get)
        st.success(f"✨ 오늘의 추천: **{best}**! (점수: {score})")
        if best == "물리학":
            st.info("⚛️ 수학으로 세상을 해석하는 재미! 로보틱스/엔지니어링과 찰떡.")
        elif best == "화학":
            st.info("🧪 실험으로 물질의 비밀을 푸는 짜릿함! 신소재/제약/반도체 진로와 굿매치.")
        elif best == "생명과학":
            st.info("🧬 생명 시스템을 데이터로 이해! 의생명·바이오 분야와 연결되기 좋아요.")
        else:
            st.info("🌍 지구 시스템을 데이터로! 기상/천문/환경 문제 해결에 적합.")

# FAQ 섹션
if nav == "FAQ":
    st.markdown("<h2 class='gtitle'>FAQ ❓ 자주 묻는 질문</h2>", unsafe_allow_html=True)
    with st.expander("Q. 수학이 약한데 물리/화학 들어도 될까요? 🧮"):
        st.write("충분히 가능! 개념을 시각화하고 문제를 구조화하는 연습부터 시작하면 됩니다. 필요하면 보충 학습 루트도 제공해요.")
    with st.expander("Q. 실험 장비가 부족하면 어떻게 하나요? 🔧"):
        st.write("저비용 대체 실험, 오픈데이터 분석, 시뮬레이션으로 충분히 탐구 가능! 보고서·발표 역량이 핵심입니다.")
    with st.expander("Q. 의학/AI/반도체 진로엔 어떤 과목이 유리하죠? 🧭"):
        st.write("의학·바이오 → 생명과학/화학, AI·로보틱스 → 물리학, 반도체·신소재 → 화학/물리학, 기상·환경·천문 → 지구과학.")

# 고정 하단 CTA
st.markdown("""
<div class='card'>
  <h3>📌 마지막 한 줄 요약</h3>
  <p>✨ <b>재미있는 과목이 곧 잘하는 과목</b>이 됩니다. 오늘 가장 끌리는 탭부터 들어가 보세요! ⚛️🧪🧬🌍</p>
</div>
""", unsafe_allow_html=True)
