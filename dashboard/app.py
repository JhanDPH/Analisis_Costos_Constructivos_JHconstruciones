import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

st.set_page_config(page_title="Dashboard Constructivo", layout="wide")

# =========================
# 📂 CARGAR DATA
# =========================
df = pd.read_csv('data/costos_final_limpio.csv')

df['fecha_inicio'] = pd.to_datetime(df['fecha_inicio'], errors='coerce')
df['costo_total'] = df['costo_material'] + df['costo_mano_obra']

# =========================
# 🎛️ FILTROS (SEGMENTACIÓN)
# =========================
st.sidebar.header("Filtros")

tipo = st.sidebar.multiselect(
    "Tipo de Proyecto",
    options=df['tipo_proyecto'].unique(),
    default=df['tipo_proyecto'].unique()
)

ciudad = st.sidebar.multiselect(
    "Ciudad",
    options=df['ciudad'].unique(),
    default=df['ciudad'].unique()
)

df = df[
    (df['tipo_proyecto'].isin(tipo)) &
    (df['ciudad'].isin(ciudad))
]

# =========================
# 📊 KPIs
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Costo Total", f"${df['costo_total'].sum():,.0f}")
col2.metric("Costo Promedio", f"${df['costo_total'].mean():,.0f}")
col3.metric("Retraso Promedio", f"{df['retraso_dias'].mean():.1f} días")
col4.metric("Proyectos", df['nombre_proyecto'].nunique())

st.markdown("---")

# =========================
# 📊 COSTO POR PROYECTO
# =========================
st.subheader("Costo por Proyecto")

df_proj = df.groupby('nombre_proyecto')['costo_total'].sum()

st.bar_chart(df_proj)

# =========================
# 📊 DISTRIBUCIÓN COSTOS
# =========================
st.subheader("Distribución de Costos")

costos = df[['costo_material','costo_mano_obra']].sum()

fig, ax = plt.subplots()
ax.pie(costos, labels=['Material','Mano de obra'], autopct='%1.1f%%')
st.pyplot(fig)

# =========================
# 📊 COSTO POR FASE
# =========================
st.subheader("Costo por Fase")

fase = df.groupby('fase')['costo_total'].sum()
st.bar_chart(fase)

# =========================
# 📊 RETRASOS
# =========================
st.subheader("Retraso por Proyecto")

retraso = df.groupby('nombre_proyecto')['retraso_dias'].mean()
st.bar_chart(retraso)

# =========================
# 📈 EVOLUCIÓN TIEMPO
# =========================
st.subheader("Evolución de Costos")

costos_mes = (
    df.set_index('fecha_inicio')
    .resample('ME')['costo_total']
    .sum()
)

st.line_chart(costos_mes)

# =========================
# 🔮 PROYECCIÓN
# =========================
st.subheader("Proyección (Tendencia)")

y = costos_mes.values
x = np.arange(len(y))

coef = np.polyfit(x, y, 1)
proy = np.polyval(coef, len(y))

st.write(f"Proyección siguiente periodo: ${proy:,.0f}")