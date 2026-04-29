# 🏗️ Análisis de Costos en Proyectos Constructivos

## 📊 Descripción del Proyecto

Este proyecto presenta un análisis integral de costos en proyectos de construcción, con el objetivo de evaluar el desempeño financiero, identificar desviaciones presupuestarias y analizar la relación entre tiempo, fases constructivas y gasto total.

El análisis incluye limpieza de datos, exploración, visualización y desarrollo de un dashboard interactivo.

---

## 🎯 Objetivos

### 🔹 Objetivo General

Analizar el comportamiento de los costos en proyectos constructivos para identificar patrones, riesgos y oportunidades de optimización.

### 🔹 Objetivos Específicos

* Evaluar la distribución de costos (materiales vs mano de obra)
* Analizar desviaciones entre costos estimados y reales
* Identificar las fases más costosas del proyecto
* Evaluar la relación entre duración y costo
* Analizar retrasos en ejecución

---

## 📂 Estructura del Proyecto

```
Analisis_Costos_Constructivos/
│
├── data/
│   ├── costos_final.csv
│
├── notebooks/
│   ├── analisis_costos.ipynb
│
├── images/
│   ├── distribucion_costos.png
│   ├── costos_mes.png
│   ├── costos_fase.png
│   ├── desviacion.png
│   ├── scatter.png
│
├── dashboard/
│   ├── app.py
│
└── README.md
```

---

## ⚙️ Tecnologías Utilizadas

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## 🧹 Procesamiento de Datos

Se realizaron las siguientes transformaciones:

* Limpieza y estandarización de columnas
* Conversión de fechas
* Eliminación de decimales innecesarios
* Creación de variables derivadas (costo_total)
* Normalización de porcentajes

---

## 📊 Análisis Realizado

El proyecto incluye:

* 📌 Distribución de costos (materiales vs mano de obra)
* 📈 Evolución de costos en el tiempo
* 🏗️ Costos por fase del proyecto
* 📉 Desviación por proyecto
* ⏱️ Relación entre duración y costo
* ⚠️ Análisis de retrasos

---

## 📊 Dashboard Interactivo

Se desarrolló un dashboard utilizando Streamlit que permite:

* Visualizar KPIs principales
* Filtrar por proyecto
* Analizar costos por fase
* Observar evolución de costos en el tiempo

---

## 🚀 Cómo Ejecutar el Proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/JhanDPH/Analisis_Costos_Constructivos_JHconstruciones.git
cd Analisis_Costos_Constructivos_JHconstrucciones/
```

---

### 2️⃣ Entrar a entorno virtual

```bash
# Crear entorno
conda create -n costos_construccion python=3.13

# Activar entorno
conda activate costos_construccion

```

---

### 3️⃣ Instalar dependencias

Si no tienes el archivo requirements:

```bash
pip conda install pandas numpy matplotlib seaborn streamlit
```

---

### 4️⃣ Ejecutar el Notebook

Abrir:

```
notebooks/analisis_costos.ipynb
```

---

### 5️⃣ Ejecutar el Dashboard

```bash
 streamlit run dashboard/app.py
```

---

## 📌 Principales Hallazgos

* Los proyectos presentan **sobrecostos leves (4% - 6%)**
* Las fases más costosas son **estructura y obra gris**
* Existe una relación directa entre **duración y costo**
* Los retrasos son bajos, indicando buena gestión operativa

---

## ⚠️ Limitaciones

* Datos simulados / generados parcialmente
* No incluye variables externas (inflación, clima real, etc.)
* Puede mejorarse con datos en tiempo real

---

## 🚀 Mejoras Futuras

* Integración con bases de datos reales
* Dashboard avanzado con filtros dinámicos
* Predicción de costos con Machine Learning
* Automatización de reportes

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas.

Si deseas mejorar este proyecto:

1. Haz un fork del repositorio
2. Crea una nueva rama
3. Realiza tus cambios
4. Envía un pull request

---

## 📬 Contacto

Si deseas contactarme o conocer más sobre este proyecto:

* LinkedIn: (tu perfil)
* GitHub: (tu usuario)

---

## ⭐ Nota Final

Este proyecto fue desarrollado como parte de un portafolio practico en análisis de datos, enfocado en resolver problemas reales del sector construcción mediante herramientas de ciencia de datos.

---
