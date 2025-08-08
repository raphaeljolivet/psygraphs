import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import plot

def initial_data() :
    data = {
       "ICV": 108,
       "IVS": 91,
        "IRF" : 101,
        "IMT": 93,
        "IVT": 68,
        "QIT": 93}

    scores =  pd.DataFrame.from_dict(data, orient='index', columns=['score']).reset_index()
    scores.columns = ['indice', 'score']
    return scores

def main():
    st.title("Notes composites")

    df = initial_data()
    df = st.data_editor(df, hide_index=True, column_order=["cat", "indice", "score"])
    df = df.set_index(['indice'])

    plt = plot(
        df,
        title="Profil des notes composites",
        yrange=[40, 160],
        line1=15, line2=30,
        width=8)
    st.pyplot(plt)

st.set_page_config(page_title="Notes composites")
main()

