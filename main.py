import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="원달러 환율 변화", page_icon="💱", layout="wide")

# 제목
st.title("💱 최근 10년간 원달러 환율 변화")

# 데이터 가져오기
@st.cache_data
def get_exchange_rate_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*10)
    
    # Yahoo Finance에서 USD/KRW 환율 데이터 가져오기
    data = yf.download("USDKRW=X", start=start_date, end=end_date)
    return data

# 데이터 로드
df = get_exchange_rate_data()

# 데이터 전처리
df = df.reset_index()
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Close']]
df.columns = ['날짜', '환율']

# 그래프 그리기
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['날짜'], df['환율'])
ax.set_xlabel('날짜')
ax.set_ylabel('원/달러 환율')
ax.set_title('최근 10년간 원달러 환율 변화')
plt.xticks(rotation=45)
plt.grid(True)

# Streamlit에 그래프 표시
st.pyplot(fig)

# 데이터 표시
st.subheader("원달러 환율 데이터")
st.dataframe(df)

# 통계 정보
st.subheader("환율 통계")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("최근 환율", f"{df['환율'].iloc[-1]:.2f} 원", f"{df['환율'].iloc[-1] - df['환율'].iloc[-2]:.2f}")
with col2:
    st.metric("10년 최고 환율", f"{df['환율'].max():.2f} 원")
with col3:
    st.metric("10년 최저 환율", f"{df['환율'].min():.2f} 원")
