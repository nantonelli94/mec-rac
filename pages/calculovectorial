import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración básica
st.set_page_config(page_title="Módulo 1: Cálculo Vectorial", layout="wide")

st.title("📐 Módulo 1: Fundamentos y Cálculo Vectorial")
st.write("Introducción conceptual al álgebra de vectores aplicada a la mecánica.")

# Pestañas para separar Teoría de los Ejercicios de tus PPTX
tab1, tab2 = st.tabs(["📖 Teoría Básica", "📝 Ejercicios de Aplicación"])

with tab1:
    st.subheader("1.1 Representación de Vectores")
    st.write("Un vector en el espacio tridimensional se define por sus componentes:")
    st.latex(r"\mathbf{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}")
    
    st.info("⚡ [PLACEHOLDER]: Aquí puedes añadir explicaciones sobre producto escalar y vectorial.")

with tab2:
    st.subheader("Ejercicios Prácticos Extraídos de Diapositivas")
    
    with st.expander("Problema 1: Cálculo del vector resultante (Ver Solución)"):
        st.write("**Enunciado:** Dos fuerzas $\mathbf{F_1}$ y $\mathbf{F_2}$ actúan sobre un mismo punto. Calcular la fuerza resultante.")
        st.latex(r"\mathbf{F_1} = 3\hat{i} + 4\hat{j} \quad \text{y} \quad \mathbf{F_2} = -1\hat{i} + 2\hat{j}")
        
        st.write("**Desarrollo:**")
        st.latex(r"\mathbf{F_R} = (3 - 1)\hat{i} + (4 + 2)\hat{j} = 2\hat{i} + 6\hat{j}")
        st.success("✅ **Resultado:** La fuerza neta es $\mathbf{F_R} = 2\hat{i} + 6\hat{j}\text{ N}$.")
        
    st.caption("✏️ [PLACEHOLDER]: Añade aquí más desplegables ejecutando el script extractor de tus PPTX.")
