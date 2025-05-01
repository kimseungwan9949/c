
import streamlit as st
import os
import random

st.set_page_config(page_title="TWO Y FIT 맞춤 루틴 생성기", layout="centered")
st.image("two_y_fit_logo_transparent.png", width=200)
st.title("TWO Y FIT 맞춤 루틴 생성기")

routine_db = {
    "어깨": [
        ("오버헤드프레스", "오버헤드프레스.PNG"),
        ("프론트 레이즈", "프론트 레이즈.PNG"),
        ("사이드 레터럴 레이즈", "사이드 레터럴 레이즈.PNG"),
        ("덤벨 숄더프레스", "덤벨 숄더프레스.PNG"),
        ("업라이트 로우", "업라이트 로우.PNG"),
        ("페이스풀", "페이스풀.PNG"),
        ("벤트오버 레이즈", "벤트오버 레이즈.PNG"),
        ("리어 델트 플라이", "리어 델트 플라이.PNG"),
        ("밀리터리프레스", "밀리터리프레스.PNG"),
        ("슈러그", "슈러그.PNG")
    ],
    "등": [
        ("컨벤셔널 데드리프트", "컨벤셔널 데드리프트.PNG"),
        ("랫풀다운", "랫풀다운.PNG"),
        ("비하인드 랫풀다운", "비하인드 랫풀다운.PNG"),
        ("케이블 풀다운", "케이블 풀다운.PNG"),
        ("인클라인 덤벨로우", "인클라인 덤벨로우.PNG"),
        ("티바로우", "티바로우.PNG"),
        ("원암 덤벨로우", "원암 덤벨로우.PNG"),
        ("케이블 시티드로우", "케이블 시티드로우.PNG"),
        ("바벨로우", "바벨로우.PNG"),
        ("어시스트 풀업 머신", "어시스트 풀업 머신.PNG"),
        ("케이블 암풀 다운", "케이블 암풀 다운.PNG")
    ],
    "가슴": [
        ("벤치프레스", "벤치프레스.PNG"),
        ("덤벨 플랫 벤치프레스", "덤벨 플랫 벤치프레스.PNG"),
        ("인클라인 벤치프레스", "인클라인 벤치프레스.PNG"),
        ("인클라인 덤벨 프레스", "인클라인 덤벨 프레스.PNG"),
        ("덤벨 풀오버", "덤벨 풀오버.PNG"),
        ("펙덱 플라이", "펙덱 플라이.PNG"),
        ("인클라인 덤벨 플라이", "인클라인 덤벨 플라이.PNG"),
        ("케이블 크로스 오버", "케이블 크로스 오버.PNG"),
        ("덤벨 플라이", "덤벨 플라이.PNG"),
        ("어시스트 딥스 머신", "어시스트 딥스 머신.PNG"),
        ("푸쉬업", "푸쉬업.PNG")
    ],
    "하체": [
        ("스쿼트", "바벨 스쿼트.PNG"),
        ("프론트 스쿼트", "프론트 스쿼트.PNG"),
        ("고블릿 스쿼트", "고블릿 스쿼트.PNG"),
        ("브이스쿼트", "브이스쿼트.PNG"),
        ("리버스 브이스쿼트", "리버스 브이스쿼트.PNG"),
        ("런지", "런지.PNG"),
        ("불가리안 스플릿 스쿼트", "불가리안 스플릿 스쿼트.PNG"),
        ("레그 프레스", "레그 프레스.PNG"),
        ("레그 익스텐션", "레그 익스텐션.PNG"),
        ("레그컬", "레그컬.PNG"),
        ("이너타이", "이너타이.PNG"),
        ("아웃타이", "아웃타이.PNG"),
        ("스티프 데드리프트", "스티프 데드리프트.PNG"),
        ("백 익스텐션", "백 익스텐션.PNG"),
        ("힙 쓰러스트", "힙 쓰러스트.PNG"),
        ("카프레이즈", "카프레이즈.PNG")
    ]
}

arms_db = {
    "이두": [
        ("덤벨 해머컬", "덤벨 해머컬.PNG"),
        ("덤벨컬", "덤벨컬.PNG"),
        ("바벨컬", "바벨컬.PNG"),
        ("스파이더 컬", "스파이더 컬.PNG"),
        ("인클라인 덤벨 컬", "인클라인 덤벨 컬.PNG"),
        ("컨센트레이션 컬", "컨센트레이션 컬.PNG"),
        ("케이블 로프 해머컬", "케이블 로프 해머컬.PNG"),
        ("케이블 바벨 컬", "케이블 바벨 컬.PNG")
    ],
    "삼두": [
        ("라잉 트라이셉스 익스텐션", "라잉 트라이셉스 익스텐션.PNG"),
        ("시티드 트라이셉스 익스텐션", "시티드 트라이셉스 익스텐션.PNG"),
        ("케이블 트라이셉스 푸쉬 다운", "케이블 트라이셉스 푸쉬 다운.PNG"),
        ("원 암 트라이셉 익스텐션", "원 암 트라이셉 익스텐션.PNG"),
        ("케이블 오버헤드 트라이셉 익스텐션", "케이블 오버헤드 트라이셉 익스텐션.PNG"),
        ("케이블 로프 오버헤드 트라이셉 익스텐션", "케이블 로프 오버헤드 트라이셉 익스텐션.PNG"),
        ("킥 백", "킥 백.PNG")
    ]
}

main_exercise = {
    "어깨": "오버헤드프레스",
    "등": "컨벤셔널 데드리프트",
    "가슴": "벤치프레스",
    "하체": "스쿼트"
}

part = st.selectbox("운동 부위 선택", ["어깨", "등", "가슴", "하체", "팔"])

if part == "팔":
    arm_type = st.radio("세부 부위 선택", ["이두", "삼두"])
    st.markdown("**3세트 / 15회 기준으로 추천됩니다.**")
    st.markdown("📌 운동 루틴 생성 후 순서는 그대로 해도 되고 바꿔도 상관 없습니다.")
    selected = random.sample(arms_db[arm_type], 4)
    for i, (name, file) in enumerate(selected, 1):
        col1, col2 = st.columns([1, 5])
        with col1:
            if os.path.exists(file):
                st.image(file, width=150)
            else:
                st.warning("이미지 없음")
        with col2:
            st.markdown(f"**{i}. {name}**  \n3세트 / 15회")
else:
    experience = st.selectbox("운동 경력", ["1개월~1년 미만", "1년 이상"])
    if experience == "1개월~1년 미만":
        num_exercises = 4
        reps = "15회"
        sets = 4
    else:
        num_exercises = 6
        reps = "15~20회"
        sets = random.choice([4, 5])

    all_items = routine_db[part]
    main_name = main_exercise.get(part, "")
    main_item = [e for e in all_items if e[0] == main_name]
    others = [e for e in all_items if e not in main_item]
    random.shuffle(others)
    final = main_item + others[:num_exercises - len(main_item)]
    random.shuffle(final[:2])

    st.markdown("📌 운동 루틴 생성 후 순서는 그대로 해도 되고 바꿔도 상관 없습니다.")
    st.markdown("💥 <span style='color:red;'>💥 메인운동은 무게가 무거워질수록 반복 횟수를 줄입니다.</span>", unsafe_allow_html=True)

    for i, (name, file) in enumerate(final, 1):
        is_main = name == main_name
        rep_text = "8~10회" if is_main else reps
        prefix = "💥 " if is_main else ""
        col1, col2 = st.columns([1, 5])
        with col1:
            if os.path.exists(file):
                st.image(file, width=150)
            else:
                st.warning("이미지 없음")
        with col2:
            st.markdown(f"**{i}. {prefix}{name}**  \n{sets}세트 / {rep_text}")
