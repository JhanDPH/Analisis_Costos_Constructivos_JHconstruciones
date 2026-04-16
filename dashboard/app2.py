import streamlit as st

st.title("Dashboard Costos Constructivos")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Costo Total", f"${df['costo_real'].sum()/1e9:.2f}B")
col2.metric("Desviación Promedio", f"{df['porcentaje_desviacion'].mean():.2f}%")
col3.metric("Sobrecostos", f"${df[df['diferencia_costo']>0]['diferencia_costo'].sum()/1e9:.2f}B")

# Filtro
tipo = st.selectbox("Tipo de obra", df['tipo_obra'].unique())

df_filtrado = df[df['tipo_obra'] == tipo]

st.bar_chart(df_filtrado.groupby('fase')['costo_real'].sum())