import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# 데이터 준비 (예시 데이터)
data = {
    'Year': list(range(2010, 2021)),
    'CO2_Emissions': [32.5, 33.1, 33.8, 34.2, 34.5, 34.8, 35.0, 35.2, 35.5, 35.7, 35.3],
    'Renewable_Energy': [8.7, 9.2, 9.8, 10.5, 11.2, 11.9, 12.6, 13.4, 14.2, 15.1, 16.0],
    'Forest_Area': [40.2, 40.1, 40.0, 39.9, 39.8, 39.7, 39.6, 39.5, 39.4, 39.3, 39.2]
}

df = pd.DataFrame(data)

# 퀴즈 문제 정의
quiz_data = [
    {
        "question": "2020년 CO2 배출량은 얼마인가요?",
        "options": ["34.5", "35.3", "35.7", "36.0"],
        "correct": "35.3",
        "data_key": "CO2_Emissions"
    },
    {
        "question": "재생에너지 사용 비율이 가장 높은 해는?",
        "options": ["2018", "2019", "2020", "2021"],
        "correct": "2020",
        "data_key": "Renewable_Energy"
    },
    {
        "question": "산림 면적이 가장 넓었던 해는?",
        "options": ["2010", "2015", "2018", "2020"],
        "correct": "2010",
        "data_key": "Forest_Area"
    }
]

# Streamlit 앱 시작
st.title("환경 데이터 시각화 퀴즈")

# 세션 상태 초기화
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0

# 현재 문제 표시
if st.session_state.current_question < len(quiz_data):
    question = quiz_data[st.session_state.current_question]
    
    # 데이터 시각화
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['Year'], df[question['data_key']])
    ax.set_xlabel('Year')
    ax.set_ylabel(question['data_key'].replace('_', ' '))
    ax.set_title(f'{question["data_key"].replace("_", " ")} Trend')
    st.pyplot(fig)
    
    st.write(f"문제 {st.session_state.current_question + 1}: {question['question']}")
    
    # 사용자 응답
    user_answer = st.radio("답을 선택하세요:", question['options'])
    
    if st.button("다음 문제"):
        if user_answer == question['correct']:
            st.session_state.score += 1
        st.session_state.current_question += 1

# 퀴즈 종료 후 결과 표시
if st.session_state.current_question == len(quiz_data):
    st.write(f"퀴즈가 종료되었습니다. 당신의 점수는 {len(quiz_data)}점 만점에 {st.session_state.score}점입니다.")
    if st.button("퀴즈 다시 시작"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.experimental_rerun()
