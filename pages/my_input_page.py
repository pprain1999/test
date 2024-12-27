import streamlit as st
import pandas as pd

st.title("사용자 정보 입력")

name = st.text_input("이름")
zs_option = ["쌍둥이자리","천칭자리", "사자자리", "물고기자리", "물병자리", "게자리", "황소자리", "처녀자리", "사수자리", "양자리", "전갈자리", "염소자리"]

zodiac_sign = st.selectbox("별자리", zs_option)

col1, col2 = st.columns(2)
with col1:
    if st.button("별자리 모름", icon="😥"):
        st.caption("인터넷에 검색해보세요...!")
        if st.link_button("검색해보러가기", "https://www.google.com/search?q=%EB%B3%84%EC%9E%90%EB%A6%AC+%EB%82%A0%EC%A7%9C&oq=%EB%B3%84%EC%9E%90%EB%A6%AC+%EB%82%A0%EC%A7%9C&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIKCAIQABiABBiiBDIICAMQABgFGB4yCggEEAAYBRgKGB4yCAgFEAAYBRgeMgoIBhAAGIAEGKIE0gEINDkyN2owajeoAgewAgE&sourceid=chrome&ie=UTF-8", icon= "🔍",):
            pass
        elif st.button("표에서 찾아보기", icon="🔍"):
            data = pd.DataFrame({ 
                    "별자리": ["쌍둥이자리","천칭자리","사자자리","물고기자리","물병자리","게자리","황소자리","처녀자리","사수자리"," 양자리"," 전갈자리"," 염소자리"],
                    "생일": ["5월 21일~6월 21일","9월 23일~10월 22일","7월 23일~8월 22일","2월 19일~3월 20일","1월 20일~2월 18일","6월 22일~7월 22일","4월 20일~5월 20일","8월 23일~9월 22일","11월 23일~12월 21일","3월 21일~4월 19일","10월 23일~11월 22일","12월 22일~1월 19일"]})
            st.dataframe(data)

# if st.button("표에서 찾아보기", icon="🔍"):
#             data = pd.DataFrame({ 
#                     "별자리": ["쌍둥이자리","천칭자리","사자자리","물고기자리","물병자리","게자리","황소자리","처녀자리","사수자리"," 양자리"," 전갈자리"," 염소자리"],
#                     "생일": ["5월 21일~6월 21일","9월 23일~10월 22일","7월 23일~8월 22일","2월 19일~3월 20일","1월 20일~2월 18일","6월 22일~7월 22일","4월 20일~5월 20일","8월 23일~9월 22일","11월 23일~12월 21일","3월 21일~4월 19일","10월 23일~11월 22일","12월 22일~1월 19일"]})
#             st.dataframe(data)
# with col1:
#     if st.button("별자리 모름", icon="😥"):
#         d = st.date_input("생일을 입력하세요", value=None)
with col2:
    if st.button("별자리 운세 알아보기!", icon="😊"):
        st.write(f"{zodiac_sign}인 {name}님의 오늘 운세는...")

