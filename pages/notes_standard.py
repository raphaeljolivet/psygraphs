import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import plot

def initial_data() :
    data = {
        "Comp. verbale": {
            "INF": 10,
            "SIM": 13,
            "VOC": 12,
            "COS": 15
        },
        "Visuo-spatiale": {
            "CUB": 14,
            "AOB": 10
        },
        "Rais. fluide": {
            "MAT": 7,
            "IDC": 10
        },
        "Mém. de travail": {
            "REC": 10,
            "MSP": 7
        },
        "Vitesse trait.": {
            "SYM": 7,
            "BAR": 4,
            "COD": 5
        }
    }

    scores = pd.DataFrame.from_dict(data).stack().reset_index()
    scores.columns = ['indice', 'cat', 'score']
    return scores

def main():
    st.title("Hello world")

    df = initial_data()
    df = st.data_editor(df, hide_index=True, column_order=["cat", "indice", "score"])
    df = df.set_index(['cat', 'indice'])

    plt = plot(
        df,
        title="Profil des notes standard",
        yrange=(1, 19),
        line1=3, line2=6, width=8)
    st.pyplot(plt)


st.set_page_config(page_title="Notes standard")
main()