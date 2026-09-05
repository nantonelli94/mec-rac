import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración obligatoria en la primera línea
st.set_page_config(page_title="Módulo 3: Masa Variable", layout="wide")

st.title("⚖️ Módulo 3: Sistemas de Masa Variable")
st.write("Estudio de sistemas dinámicos donde la masa cambia en función del tiempo.")

# Estructura de pestañas: Teoría y tu ejercicio de examen
tab1, tab2 = st.tabs(["📖 Teoría Breve", "📝 Ejercicio Resuelto (UTN 2024)"])

# ==========================================
# PESTAÑA 1: TEORÍA BREVE
# ==========================================
with tab1:
    st.header("Sistemas de Masa Variable")
    st.write("""
    En la mecánica clásica, la segunda ley de Newton se generaliza para sistemas donde la masa no es constante, 
    como cohetes que expulsan combustible o contenedores que pierden líquido.
    """)
    
    st.subheader("La Ecuación Fundamental")
    st.write("La ecuación de movimiento para un cuerpo de masa variable $m(t)$ es:")
    st.latex(r"\mathbf{F}_{\text{ext}} + \mathbf{v}_{\text{rel}} \frac{dm}{dt} = m \frac{d\mathbf{v}}{dt}")
    
    st.markdown(r"""
    Donde:
    * $\mathbf{F}_{\text{ext}}$: Sumatoria de fuerzas externas que actúan sobre el cuerpo (gravedad, fricción, etc.).
    * $\mathbf{v}_{\text{rel}}$: Velocidad relativa con la que la masa entra o sale del sistema respecto al cuerpo.
    * $\frac{dm}{dt}$: Tasa de cambio de la masa en el tiempo (positiva si entra, negativa si sale).
    """)
    
    st.subheader("Casos Especiales")
    st.info(r"""
    💡 **Expulsión Lateral u Horizontal:** Si la masa se desprende de forma estrictamente perpendicular 
    a la dirección del movimiento principal, la velocidad relativa en el eje de movimiento es cero ($\mathbf{v}_{\text{rel}} = 0$). 
    En este caso, no se genera una fuerza de propulsión (*empuje*) en el eje del movimiento, reduciendo la ecuación a:
    $$ \mathbf{F}_{\text{ext}} = m(t) \cdot \mathbf{a} $$
    """)

# ==========================================
# PESTAÑA 2: EJERCICIO RESUELTO
# ==========================================
with tab1 if False else tab2:
    st.header("Ejercicio: Contenedor con Masa Variable")
    st.caption("Evaluado en el examen parcial de Mecánica Racional - UTN FRMDP (Cursada 2024)")
    
    st.subheader("Enunciado")
    st.write("""
    Se tiene un contenedor $C$ de masa despreciable conectado a un bloque $B$ de masa a través de una cuerda 
    inextensible y de masa despreciable, y una polea de inercia despreciable. Se llena $C$ con 5 kg de masa de agua 
    y se libera del reposo. El sistema comienza a moverse mientras el agua se filtra por varios pequeños agujeros 
    justo por encima de la base del contenedor a una tasa constante de $0.175\text{ kg/s}$. 
    
    Asumiendo que el agua se filtra únicamente en dirección horizontal y que el movimiento del contenedor es vertical 
    en todo momento, y sabiendo que el bloque $B$ está sometido a una fricción constante con el suelo de $36.75\text{ N}$, 
    **calcule la velocidad máxima del sistema**.
    """)
    
    # Manejo de la imagen del enunciado
    try:
        st.image("img/e_mv.jpg", caption="Figura 1: Enunciado del ejercicio de masa variable.", width=500)
    except:
        st.warning("⚠️ [Aviso de GitHub]: Sube la imagen del enunciado en la ruta 'img/e_mv.jpg' de tu repositorio para que se visualice aquí.")

    st.subheader("Resolución Paso a Paso")
    
    st.write("""
    Es un problema de masa variable dado que la masa del bloque $C$ es función del tiempo. Por otra parte, 
    no se consideran fuerzas de propulsión porque la masa es expulsada en dirección horizontal, por tanto 
    no afecta a la dirección de movimiento de dicho bloque (vertical).
    
    Primero, se debe explicitar la masa de $C$ en función del tiempo. La tasa de expulsión es constante, 
    y la denominaremos $\alpha$:
    """)
    st.latex(r"m_c = m_{c0} - \alpha \cdot t")
    
    st.write("Se plantean diagramas de cuerpo libre de ambos cuerpos y se aplica la segunda ley de Newton.")
    
    st.markdown("**Del diagrama de cuerpo libre de B, se obtiene:**")
    st.latex(r"\sum F_x = T - F_r = m_b \cdot a")
    
    st.markdown("**Del diagrama de cuerpo libre de C, se obtiene:**")
    st.latex(r"\sum F_y = m_c g - T = m_c \cdot a")
    
    st.write("Reemplazando la tensión $T$ obtenida de la segunda ecuación en la primera ecuación, resulta:")
    st.latex(r"m_c \cdot g - (F_r + m_b \cdot a)  = m_c \cdot a")
    
    st.write("Operando algebraicamente para despejar la aceleración ($a$):")
    st.latex(r"a = \frac{m_c \cdot g - F_r}{m_b + m_c}")
    
    st.write("Nótese que el enunciado indica de forma implícita:")
    st.latex(r"F_r = 3.75 \cdot g \quad (\text{Dado que } 36.75\text{ N} / 9.8\text{ m/s}^2 = 3.75\text{ kg})")
    
    st.write("Sustituyendo los valores numéricos del problema en el Sistema Internacional (SI):")
    st.latex(r"""
    \begin{aligned}
    m_b &= 5 \\
    \alpha &= 0.175 \\
    m_{c0} &= 5 \\
    m_c &= 5 - 0.175t
    \end{aligned}
    """)
    
    st.write("Reemplazando los valores en la ecuación de la aceleración:")
    st.latex(r"a = g \frac{5 - 0.175t - 3.75}{5 + 5 - 0.175t}")
    
    st.write("Simplificando la expresión fraccionaria:")
    st.latex(r"a = g \left( 1 - \frac{8.75}{10 - 0.175t} \right)")
    
    st.write("Llegado a este punto, integramos la aceleración respecto al tiempo para obtener la velocidad ($v$):")
    st.latex(r"v = \int a \, dt = \int g \left( 1 - \frac{8.75}{10 - 0.175t} \right) dt")
    st.latex(r"v - v_0 = g \left[ t - \left( -\frac{8.75}{0.175} \ln(10 - 0.175t) \right) \right]_{t_0}^{t_f}")
    
    st.subheader("Cálculo del Tiempo de Velocidad Máxima")
    st.write("""
    Para hallar el instante en que la velocidad es máxima, buscamos el punto donde la aceleración se anula ($a = 0$). 
    Igualando la expresión analítica a cero:
    """)
    st.latex(r"\frac{8.75}{10 - 0.175t} = 1")
    st.write("Despejando el tiempo final resulta: $t_f \approx 7.143\\text{ segundos}$.")
    st.write("Considerando las condiciones iniciales de reposo: $t_0 = 0$ y $v_0 = 0$.")
    
    st.write("Evaluando los límites en la ecuación integrada de la velocidad:")
    st.latex(r"v_f = 9.8 \left( 7.143 + \left[ \frac{8.75}{0.175} \ln(10 - 0.175 \cdot 7.143) - \ln(10) \right] \right)")
    
    st.write("Operando numéricamente los logaritmos, obtenemos el resultado definitivo:")
    st.success(r"✅ **Resultado Final:** La velocidad máxima alcanzada por el sistema es $v_f \approx 4.57\text{ m/s}$.")
