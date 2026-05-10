import streamlit as st 

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("Advanced Analytics")

st.divider()

st.subheader("Weekly activity")

st.line_chart(
    [1000,4000,7000,9800]
)


st.subheader("calories overview")

st.bar_chart([
    100,
    250,
    400
])
