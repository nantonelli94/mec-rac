import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración obligatoria en la primera línea
st.set_page_config(page_title="Módulo 2: Dinámica", layout="wide")

st.title("🏋️ Módulo 2: Dinámica de la Partícula")
st.write("Estudio de las causas que producen el movimiento y modelado de fuerzas reales.")

# Pestañas del módulo
tab1, tab2 = st.tabs(["📖 Teoría Breve", "🕹️ Simulador: Tiro con Resistencia del Aire"])

# ==========================================
# PESTAÑA 1: TEORÍA BREVE
# ==========================================
with tab1:
    st.header("Dinámica Newtoneana y Fuerzas de Fricción Fluida")
    st.write("""
    A diferencia de la cinemática pura o de los modelos idealizados del vacío presentes en textos clásicos 
    como el Hertig, la dinámica real de un cuerpo en la atmósfera exige considerar las fuerzas de arrastre o 
    resistencia del fluido (fricción aerodinámica).
    """)
    
    st.subheader("1. Segunda Ley de Newton")
    st.write("La ley fundamental del movimiento se expresa vectorialmente como:")
    st.latex(r"\sum \mathbf{F} = m \cdot \mathbf{a}")
    
    st.subheader("2. Modelado de la Resistencia del Aire")
    st.write("""
    Cuando un cuerpo se mueve a través de un fluido (como el aire), experimenta una fuerza opuesta al vector 
    velocidad $\mathbf{v}$. Dependiendo del régimen de velocidad (número de Reynolds), esta fuerza se modela de dos formas:
    """)
    
    st.markdown(r"""
    * **Resistencia Lineal (Velocidades bajas / Flujo laminar):**
      $$ \mathbf{F}_r = -b \cdot \mathbf{v} $$
      Donde $b$ es el coeficiente de arrastre lineal.
    * **Resistencia Cuadrática (Velocidades altas / Flujo turbulento):**
      $$ \mathbf{F}_r = -c \cdot v \cdot \mathbf{v} \quad \text{o en módulo} \quad F_r = c \cdot v^2 $$
      Donde $c = \frac{1}{2} C_d \rho A$ ($C_d$: coef. de arrastre, $\rho$: densidad del aire, $A$: área transversal).
    """)
    
    st.subheader("3. Ecuaciones Diferenciales del Movimiento")
    st.write("Para un proyectil lanzado bajo la gravedad y arrastre lineal, descomponemos en los ejes $x$ e $y$:")
    st.latex(r"""
    \begin{aligned}
    m \frac{dv_x}{dt} &= -b \cdot v_x \\
    m \frac{dv_y}{dt} &= -m \cdot g - b \cdot v_y
    \end{aligned}
    """)
    
    st.info("""
    💡 **Limitación Analítica:** Mientras que el caso lineal se puede resolver analíticamente usando ecuaciones diferenciales ordinarias, 
    el caso cuadrático genera un sistema acoplado no lineal que **no tiene solución analítica exacta**. 
    Es aquí donde la física computacional y métodos numéricos como el de **Euler** se vuelven indispensables para el ingeniero moderno.
    """)

# ==========================================
# PESTAÑA 2: SIMULADOR INTERACTIVO
# ==========================================
with tab1 if False else tab2:
    st.header("Simulador de Trayectorias: Vacío vs. Resistencia del Aire")
    st.write("Modifica los parámetros dinámicos en la barra lateral para recalcular el vuelo numéricamente mediante el método de Euler.")
    
    # Parámetros de control en columnas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        v0 = st.slider("Velocidad Inicial (m/s)", 10.0, 150.0, 50.0, step=5.0)
        theta_deg = st.slider("Ángulo de Lanzamiento (°)", 5.0, 85.0, 45.0, step=5.0)
    with col2:
        m = st.slider("Masa del Proyectil (kg)", 0.1, 10.0, 1.0, step=0.1)
        b_coef = st.slider("Coeficiente de Arrastre (b)", 0.0, 1.0, 0.15, step=0.01)
    with col3:
        tipo_friccion = st.selectbox("Tipo de Fricción", ["Lineal (-b·v)", "Cuadrática (-b·v²)"])
        g = 9.81  # Gravedad constante

    # --- CÁLCULO NUMÉRICO (MÉTODO DE EULER) ---
    theta = np.radians(theta_deg)
    dt = 0.005  # Paso del tiempo para alta precisión numérica
    
    # Listas para almacenar coordenadas
    # 1. Caso con Fricción
    x_f, y_f = [0.0], [0.0]
    vx_f, vy_f = v0 * np.cos(theta), v0 * np.sin(theta)
    
    # 2. Caso Vacío
    x_v, y_v = [0.0], [0.0]
    vx_v, vy_v = v0 * np.cos(theta), v0 * np.sin(theta)

    # Lazo del método numérico para fricción
    while y_f[-1] >= 0:
        v_mag = np.sqrt(vx_f**2 + vy_f**2)
        
        # Calcular fuerza de arrastre según selección
        if tipo_friccion == "Lineal (-b·v)":
            fx = -b_coef * vx_f
            fy = -m * g - b_coef * vy_f
        else:  # Cuadrática
            fx = -b_coef * v_mag * vx_f
            fy = -m * g - b_coef * v_mag * vy_f
            
        # Aceleraciones
        ax = fx / m
        ay = fy / m
        
        # Actualización de posiciones y velocidades (Euler)
        new_x = x_f[-1] + vx_f * dt
        new_y = y_f[-1] + vy_f * dt
        vx_f += ax * dt
        vy_f += ay * dt
        
        x_f.append(new_x)
        y_f.append(new_y)
        
        # Evitar bucles infinitos por errores numéricos
        if len(x_f) > 10000: break

    # Lazo del método numérico para Vacío (Ideal)
    while y_v[-1] >= 0:
        ax_v = 0
        ay_v = -g
        
        new_x_v = x_v[-1] + vx_v * dt
        new_y_v = y_v[-1] + vy_v * dt
        vx_v += ax_v * dt
        vy_v += ay_v * dt
        
        x_v.append(new_x_v)
        y_v.append(new_y_v)

    # --- GRÁFICO INTERACTIVO CON PLOTLY ---
    fig = go.Figure()
    
    # Curva Ideal (Vacío)
    fig.add_trace(go.Scatter(x=x_v, y=y_v, mode='lines', name='Vacío Teórico (Parábola Perfecta)', line=dict(color='green', dash='dash', width=3)))
    # Curva Real (Fricción)
    fig.add_trace(go.Scatter(x=x_f, y=y_f, mode='lines', name=f'Trayectoria Real ({tipo_friccion})', line=dict(color='red', width=4)))
    
    fig.update_layout(
        title="Comparativa de Trayectorias de Vuelo",
        xaxis_title="Alcance Horizontal (m)",
        yaxis_title="Altura Vertical (m)",
        xaxis=dict(range=[0, max(max(x_v), max(x_f)) * 1.05]),
        yaxis=dict(range=[0, max(max(y_v), max(y_f)) * 1.1]),
        legend=dict(yanchor="top", y=0.95, xanchor="right", x=0.95)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # --- MÉTRICAS DE RESULTADOS ---
    alcance_vacio = x_v[-1]
    alcance_friccion = x_f[-1]
    perdida_porcentaje = ((alcance_vacio - alcance_friccion) / alcance_vacio) * 100
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Alcance Máximo Teórico", f"{alcance_vacio:.2f} m")
    c2.metric(f"Alcance Real ({tipo_friccion})", f"{alcance_friccion:.2f} m", delta=f"-{(alcance_vacio - alcance_friccion):.2f} m", delta_color="inverse")
    c3.metric("Pérdida por Arrastre", f"{perdida_porcentaje:.1f} %")
