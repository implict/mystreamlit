import streamlit as st
import pandas as pd
import numpy as np

# 앱 제목 설정
st.title('My First Streamlit App')

# 간단한 텍스트 추가
st.write("Welcome to my Streamlit app!")

# 데이터프레임 생성 및 표시
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# 차트 그리기
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# 사용자 입력 받기
user_input = st.text_input("Enter your name", "Type here...")
st.write(f"Hello, {user_input}!")

# 버튼 추가
if st.button('Click me'):
    st.write('You clicked the button!')

# 선택박스 추가
option = st.selectbox(
    'What is your favorite color?',
    ['Red', 'Green', 'Blue'])
st.write('Your favorite color is ', option)
