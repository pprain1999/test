import streamlit as st
import pandas as pd

st.title("당신의 별자리 운세")

st.subheader("별자리 운세 순위표")
data = pd.DataFrame({
    "별자리": ["쌍둥이자리","천칭자리","사자자리","물고기자리","물병자리","게자리","황소자리","처녀자리","사수자리"," 양자리"," 전갈자리"," 염소자리"],
    # "운세 순위": ["1위","2위","3위","4위","5위","6위","7위","8위","9위","10위","11위","12위"]
    "운세 순위" :[ 1,2,3,4,5,6,7,8,9,10,11,12],
    "호감도": [1,21,14,13,19,51,81,31,35,56,23,76]
})

st.dataframe(data, use_container_width=True)
st.line_chart(data.set_index("별자리")["운세 순위"])

fig = data.plot.pie(
    y="호감도",
    labels=data["별자리"],
    autopct="%1.1f%%",
    figsize=(6, 6),
    legend=False,
    title="별자리 별 호감도"
).get_figure()
st.pyplot(fig)