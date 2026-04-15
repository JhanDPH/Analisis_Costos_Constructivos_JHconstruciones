import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/construction_cost_dataset_pro.csv')

st.title("Dashboard Costos Constructivos")

# KPIs
st.metric("Costo Total", df['costo_real'].sum())
st.metric("Sobrecosto Total", df['diferencia_costo'].sum())
st.metric("Retraso Promedio", round(df['retraso_dias'].mean(),2))

# Gráfica
fig = px.bar(df.groupby('fase')['costo_real'].sum().reset_index(),
             x='fase', y='costo_real', title="Costo por Fase")

st.plotly_chart(fig)