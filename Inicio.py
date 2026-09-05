import streamlit as st

# Configuración global del libro
st.set_page_config(
    page_title="Manual de Mecánica Teórica",
    page_icon="📚",
    layout="wide"
)

# Portada
st.title("📚 Manual Moderno de Mecánica Teórica")
st.subheader("Un enfoque interactivo con simulaciones y ejercicios resueltos")
st.write("---")

# Introducción
st.write("""
¡Bienvenido! Este manual está diseñado para estudiantes de física e ingeniería que buscan 
comprender los principios de la mecánica clásica no solo desde las ecuaciones, sino desde la práctica visual.
""")

# Cuadro informativo sobre cómo navegar
st.info("👈 **Cómo usar este libro:** Utiliza la barra lateral de la izquierda para navegar a través de los diferentes módulos teóricos y prácticos.")

# Índice General Estático (Para dar una vista rápida en la portada)
st.header("🗂️ Índice General del Curso")

st.markdown("""
* **Módulo 1: Fundamentos y Cálculo Vectorial**
  * Álgebra vectorial en $\mathbb{R}^3$, producto escalar y vectorial, momentos de fuerza.
* **Módulo 2: Cinemática de la Partícula**
  * Movimiento rectilíneo, tiro parabólico y componentes intrínsecas de la aceleración.
* **Módulo 3: Dinámica de Sistemas**
  * Leyes de Newton, conservación de la energía y colisiones.
* **Módulo 4: Mecánica de Fluidos**
  * Hidrostática y principios fundamentales de hidrodinámica.
""")

st.write("---")
st.caption("Desarrollado con ❤️ usando Inteligencia Artificial, Streamlit y GitHub.")
