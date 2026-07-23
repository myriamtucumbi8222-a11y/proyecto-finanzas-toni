# Dashboard financiero
# Proyecto: Industrias Lácteas Toni S.A.

import streamlit as st
import pandas as pd


# Configuración de página
st.set_page_config(
    page_title="Industrias Lácteas Toni S.A.",
    layout="wide"
)


# Título principal
st.title("Análisis Económico, Financiero y de Ingeniería Económica")

st.header("Industrias Lácteas Toni S.A.")


st.write(
    """
    Dashboard interactivo para presentar los resultados
    del análisis financiero, evaluación de inversiones,
    riesgos y valoración empresarial.
    """
)


# Indicadores principales
st.subheader("Indicadores financieros")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "VAN",
        "$0"
    )


with col2:
    st.metric(
        "TIR",
        "0%"
    )


with col3:
    st.metric(
        "WACC",
        "0%"
    )


# Escenarios
st.subheader("Escenarios")


escenarios = pd.DataFrame(
    {
        "Escenario": [
            "Optimista",
            "Base",
            "Pesimista"
        ],
        "Resultado": [
            0,
            0,
            0
        ]
    }
)


st.bar_chart(
    escenarios.set_index("Escenario")
)


# Información adicional
st.subheader("Estado del proyecto")

st.info(
    "Dashboard en desarrollo. "
    "Los indicadores serán actualizados con los resultados financieros del análisis."
)