import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Industrias Lácteas Toni S.A.",
    layout="wide"
)


st.title("Dashboard Financiero - Industrias Lácteas Toni S.A.")


# Cargar indicadores
df = pd.read_csv(
    "data/raw/processed/indicadores_financieros.csv"
)


st.subheader("Indicadores financieros")


ultimo = df.iloc[-1]


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Liquidez",
        round(ultimo["Liquidez"], 2)
    )


with col2:
    st.metric(
        "Endeudamiento",
        f"{round(ultimo['Endeudamiento']*100,2)}%"
    )


with col3:
    st.metric(
        "ROA",
        f"{round(ultimo['ROA']*100,2)}%"
    )


with col4:
    st.metric(
        "ROE",
        f"{round(ultimo['ROE']*100,2)}%"
    )


st.subheader("Evolución financiera")

st.line_chart(
    df.set_index("Año")
)