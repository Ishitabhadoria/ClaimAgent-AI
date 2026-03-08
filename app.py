import streamlit as st
import pandas as pd

from controller import run_system

st.title("Agentic AI Insurance Investigation System")

age = st.number_input("Age",20,80)
income = st.number_input("Income",20000,150000)
premium = st.number_input("Premium",5000,50000)

region = st.selectbox(
    "Region",
    ["Mumbai","Delhi","Bangalore","Chennai"]
)

hospital = st.selectbox(
    "Hospital",
    ["Apollo","Fortis","Max","Manipal"]
)

uploaded_file = st.file_uploader("Upload CSV Claim File")

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.dataframe(df)

    data = df.iloc[0].to_dict()

else:

    data = {
        "age":age,
        "income":income,
        "premium":premium,
        "region":region,
        "hospital":hospital
    }


if st.button("Run Investigation"):

    region_map = {"Mumbai":0,"Delhi":1,"Bangalore":2,"Chennai":3}
    hospital_map = {"Apollo":0,"Fortis":1,"Max":2,"Manipal":3}

    data["region"] = region_map[data["region"]]
    data["hospital"] = hospital_map[data["hospital"]]

    report = run_system(data)

    st.text(report)