import streamlit as st

pg = st.navigation(
    [st.Page(
    "pages/notes_standard.py",
    title="Notes standard"),

    st.Page(
    "pages/notes_composites.py",
    title="Notes composites"),

st.Page(
    "pages/indices_complementaires.py",
    title="Indice complémentaires")


    ])

pg.run()