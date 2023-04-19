import streamlit as st

import pandas as pd
import matplotlib as plt


st.title("Project_DTM_Assaf_and_Ori")

csv_file = st.file_uploader("SakerJunctionData_1730.csv", type=["csv"])

if csv_file is not None:
    df = pd.read_csv(csv_file)
    st.write(df)

