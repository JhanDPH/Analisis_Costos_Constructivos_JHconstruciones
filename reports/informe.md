# 🏗️ INFORME DE ANÁLISIS DE COSTOS CONSTRUCTIVOS

---

## 📌 1. RESUMEN EJECUTIVO

El presente informe analiza el comportamiento de los costos en proyectos constructivos, evaluando la eficiencia financiera y operativa a partir de variables como costos reales vs estimados, duración, fases del proyecto y retrasos.

Los resultados muestran que los proyectos presentan una ejecución controlada, con desviaciones moderadas en costos y una relación directa entre el tiempo de ejecución y el gasto total.

---

## 🎯 2. OBJETIVOS

### 🔹 Objetivo General

Analizar el desempeño de los costos en proyectos constructivos para identificar patrones, desviaciones y oportunidades de mejora.

### 🔹 Objetivos Específicos

* Evaluar la distribución de costos entre materiales y mano de obra
* Analizar desviaciones entre costos estimados y reales
* Identificar las fases más costosas del proyecto
* Evaluar la relación entre duración y costos
* Analizar retrasos en la ejecución

---

## 📂 3. DESCRIPCIÓN DEL DATASET

El dataset utilizado contiene información detallada de múltiples proyectos constructivos, incluyendo:

* Nombre del proyecto
* Tipo de proyecto (residencial/comercial)
* Fase constructiva
* Actividades y materiales
* Costos (materiales, mano de obra, total)
* Duración estimada y real
* Retrasos en días
* Fechas de inicio y finalización
* Porcentaje de desviación

Este conjunto de datos permite realizar un análisis integral del desempeño de los proyectos.

---

## 🧹 4. PROCESAMIENTO Y LIMPIEZA DE DATOS

Se realizaron los siguientes procesos:

* Conversión de fechas a formato estándar
* Eliminación de valores inconsistentes
* Estandarización de nombres de fases
* Redondeo de variables numéricas
* Creación de la variable **costo_total**
* Ajuste del porcentaje de desviación

Estos pasos garantizan la calidad y confiabilidad del análisis.

---

## 📊 5. ANÁLISIS EXPLORATORIO

---

### 🔵 5.1 Distribución de Costos

Se analizó la proporción entre el costo de materiales y mano de obra.

**Resultado:**
Los materiales representan la mayor parte del costo total, lo que indica una alta dependencia de insumos en el sector.

---

### 🟢 5.2 Evolución de Costos en el Tiempo

Se evaluó el comportamiento de los costos a lo largo del tiempo.

**Resultado:**
Se observan variaciones asociadas a las fases del proyecto, con incrementos en etapas estructurales.

---

### 🟡 5.3 Costos por Fase

Se identificaron las fases con mayor impacto económico.

**Resultado:**
Las fases más costosas corresponden a:

* Estructura
* Obra gris
* Acabados

---

### 🔴 5.4 Desviación de Costos

Se compararon los costos estimados con los reales.

**Resultado:**
Los proyectos presentan desviaciones positivas moderadas (aprox. 4% - 6%), lo que indica ligeros sobrecostos.

---

### 🟣 5.5 Relación entre Costo y Duración

Se analizó la relación entre el tiempo de ejecución y el costo total.

**Resultado:**
Existe una relación directa: a mayor duración, mayor costo.

---

### ⚫ 5.6 Retrasos

Se evaluaron los retrasos en días por proyecto.

**Resultado:**
Los retrasos son bajos y controlados, lo que refleja una adecuada planificación.

---

## 🧠 6. INSIGHTS CLAVE

* Los proyectos presentan **sobrecostos controlados**
* La fase de **obra gris y estructura concentra mayor inversión**
* Existe una relación clara entre **tiempo y costo**
* La ejecución muestra un **buen control operativo**

---

## ⚠️ 7. RIESGOS IDENTIFICADOS

* Incremento acumulativo de pequeños sobrecostos
* Dependencia de precios de materiales
* Impacto potencial de retrasos en costos finales

---

## 🚀 8. RECOMENDACIONES

* Implementar seguimiento de costos en tiempo real
* Optimizar la planificación de fases críticas
* Controlar desviaciones desde etapas tempranas
* Automatizar reportes y alertas de sobrecostos

---

## 🧾 9. CONCLUSIONES

El análisis evidencia que los proyectos presentan un desempeño estable, con desviaciones controladas y una adecuada gestión del tiempo.

Sin embargo, existen oportunidades de mejora en el control de costos en fases clave, lo que permitiría optimizar la rentabilidad y eficiencia de los proyectos.

---

## 📌 10. TRABAJO FUTURO

* Integración con datos reales en tiempo real
* Modelos predictivos de costos
* Dashboards más avanzados
* Análisis de riesgo financiero

---

## 📎 11. ANEXOS

* Gráficas generadas en el análisis
* Dashboard interactivo en Streamlit
* Dataset procesado

---
