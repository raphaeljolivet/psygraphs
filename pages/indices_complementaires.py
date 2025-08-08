import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import plot

def initial_data() :
    data = {
       "LAV": 108,
       "INV": 91,
        "LAG" : 101,
        "IEC": 93}

    scores =  pd.DataFrame.from_dict(data, orient='index', columns=['score']).reset_index()
    scores.columns = ['indice', 'score']
    return scores

def main():
    st.title("Indices complémentaires")

    df = initial_data()
    df = st.data_editor(df, hide_index=True, column_order=["cat", "indice", "score"])
    df = df.set_index(['indice'])

    plt = plot(
        df,
        title="Profil des indices complémentaires",
        yrange=[40, 160],
        line1=15, line2=30,
        width=8)

    st.pyplot(plt, use_container_width=False)


st.set_page_config(page_title="Indices complémentaires")
main()