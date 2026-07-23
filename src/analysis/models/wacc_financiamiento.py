import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Industrias Lácteas Toni S.A.",
    layout="wide"
)

st.title("Dashboard Financiero - Industrias Lácteas Toni S.A.")

# Cargar indicadores financieros
df = pd.read_csv(
    "data/raw/processed/indicadores_financieros.csv",
    encoding="utf-8-sig"
)

# Último año disponible
ultimo = df.iloc[-1]

st.subheader("Indicadores financieros")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Liquidez", f"{ultimo['Liquidez']:.2f}")

with col2:
    st.metric(
        "Endeudamiento",
        f"{ultimo['Endeudamiento'] * 100:.2f}%"
    )

with col3:
    st.metric(
        "ROA",
        f"{ultimo['ROA'] * 100:.2f}%"
    )

with col4:
    st.metric(
        "ROE",
        f"{ultimo['ROE'] * 100:.2f}%"
    )

st.subheader("Evaluación de inversión")

col5, col6, col7 = st.columns(3)

with col5:
    st.metric("VAN", "$14,048,544.23")

with col6:
    st.metric("TIR", "17.09%")

with col7:
    st.metric("WACC", "11.62%")

st.subheader("Indicadores financieros por año")

st.dataframe(df)

st.subheader("Evolución de indicadores")

st.line_chart(
    df.set_index("Año")
)