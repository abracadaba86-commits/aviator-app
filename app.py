import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aviator 10x+", layout="wide")

st.title("✈️ Aviator – Análise por Minutagem (10x+)")
st.markdown("App focado em *entradas rápidas acima de 10x*.")

file = st.file_uploader("Upload do CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.dataframe(df.head())

    cols = df.columns.tolist()
    time_col = st.selectbox("Coluna de tempo", cols)
    value_col = st.selectbox("Coluna do multiplicador", cols)

    df[ti
  me_col] = pd.to_datetime(df[time_col])
    df = df.sort_values(time_col)
    df["minuto"] = df[time_col].dt.floor("min")

    grouped = df.groupby("minuto")[value_col].mean().reset_index()

    st.subheader("📊 Média por minuto")
    fig, ax = plt.subplots()
    ax.plot(grouped["minuto"], grouped[value_col])
    st.pyplot(fig)

    threshold = st.slider("Pico mínimo (10x+)", 10.0, 100.0, 10.0)
    recent = df[df[value_col] >= threshold]

    st.metric("Total de picos 10x+", len(recent))

else:
    st.info("Faça upload do CSV para começar.")
