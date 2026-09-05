import streamlit as st

# Configuración básica
st.set_page_config(page_title="Módulo 2: Cinemática", layout="wide")

st.title("🏃 Módulo 2: Cinemática de la Partícula")
st.write("Estudio del movimiento de los cuerpos sin atender a las causas que lo producen.")

tab1, tab2 = st.tabs(["📖 Teoría Básica", "📝 Ejercicios de Aplicación"])

with tab1:
    st.subheader("2.1 Ecuaciones del Movimiento")
    st.write("Para un Movimiento Rectilíneo Uniformemente Variado (MRUV):")
    st.latex(r"x(t) = x_0 + v_0 t + \frac{1}{2}a t^2")
    
    st.info("⚡ [PLACEHOLDER]: Aquí expandiremos el contenido teórico usando IA (Tiro parabólico, movimiento circular, etc.).")

with tab2:
    st.subheader("Ejercicios de Examen (PPTX)")
    
    with st.expander("Problema 1: Tiempo de frenado de un vehículo"):
        st.write("**Enunciado:** Un automóvil frena uniformemente desde una velocidad de $20\text{ m/s}$ hasta detenerse en $4\text{ segundos}$. Determine su aceleración.")
        
        st.write("**Desarrollo:**")
        st.latex(r"v_f = v_0 + a \cdot t \implies 0 = 20 + a(4)")
        st.latex(r"a = -\frac{20}{4} = -5\text{ m/s}^2")
        st.success("✅ **Resultado:** La desaceleración es de $-5\text{ m/s}^2$.")

    with st.expander("Problema 2: Tiro Parabólico"):
        st.warning("⚠️ [PLACEHOLDER]: Próximo ejercicio por transcribir de tus diapositivas.")
