import streamlit as st 
import pandas as pd

from utills.database import(
    fetch_health_data
)

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Health History")

st.divider()

# fetch data 
data = fetch_health_data()

# Dataframe

df = pd.DataFrame(data, columns=["ID","Step Count","Sleep Hours","Water Intake"])

# show table
st.subheader("Previous records")

st.dataframe(df)