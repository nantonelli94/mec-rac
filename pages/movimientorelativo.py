import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración obligatoria en la primera línea
st.set_page_config(page_title="Módulo 3: Movimiento Relativo", layout="wide")

st.title("🛸 Módulo 3: Movimiento Relativo en Sistemas Rotantes")
st.write("Estudio de la cinemática y dinámica desde sistemas de referencia en rotación constante y fuerzas ficticias.")
st.write("---")

# Constantes físicas para el Laboratorio de Lagrange (Tierra-Luna)
G = 6.67e-11
M_T = 5.97e24
M_L = 7.35e22
R = 3.84e8
omega = np.sqrt(G * (M_T + M_L) / R**3)

# Pestañas organizativas del módulo
tab1, tab2, tab3 = st.tabs(["📖 Teoría: Teorema del Transporte", "📝 Práctica Guiada: Puntos de Lagrange", "🗺️ Laboratorio Virtual"])

# ==========================================
# PESTAÑA 1: TEORÍA GENERAL
# ==========================================
with tab1:
    st.header("Movimiento Relativo y Cambio de Referencia")
    st.write("""
    Cuando analizamos el movimiento de un cuerpo desde un sistema de referencia que gira respecto a un sistema inercial, 
    las leyes cinemáticas tradicionales cambian debido a la rotación de los ejes coordenados.
    """)
    
    st.subheader("El Teorema del Transporte")
    st.write("""
    Consideramos un sistema inercial $\mathcal{I}$ y un sistema rotante $\mathcal{R}$ con velocidad angular constante 
    $\vec{\omega} = \omega \hat{z}$. Para cualquier vector $\vec{A}$, la relación entre sus derivadas temporales en ambos sistemas es:
    """)
    st.latex(r"\left( \frac{d\vec{A}}{dt} \right)_{\mathcal{I}} = \left( \frac{d\vec{A}}{dt} \right)_{\mathcal{R}} + \vec{\omega} \times \vec{A}")
    
    st.subheader("Velocidad y Aceleración Absoluta")
    st.write("Aplicando el teorema del transporte a la posición $\vec{r}$, derivamos las ecuaciones fundamentales:")
    st.markdown("**Velocidad:**")
    st.latex(r"\vec{v}_{abs} = \vec{v}_{rel} + \vec{\omega} \times \vec{r}")
    st.markdown("**Aceleración:**")
    st.latex(r"\vec{a}_{abs} = \vec{a}_{rel} + 2\,\vec{\omega} \times \vec{v}_{rel} + \vec{\omega} \times (\vec{\omega} \times \vec{r})")

    st.subheader("Ecuación de Movimiento y Fuerzas Ficticias")
    st.write("Sustituyendo la aceleración absoluta en la Segunda Ley de Newton ($m \vec{a}_{abs} = \vec{F}_{grav}$), y reordenando los términos para el observador rotante, obtenemos:")
    st.latex(r"m \vec{a}_{rel} = \vec{F}_{grav} - 2m\,\vec{\omega} \times \vec{v}_{rel} - m\,\vec{\omega} \times (\vec{\omega} \times \vec{r})")
    
    st.info(r"""
    💡 **Identificación de Fuerzas de Inercia (Ficticias):**
    * **Fuerza de Coriolis:** $\vec{F}_C = -2m\,\vec{\omega} \times \vec{v}_{rel}$ (Solo aparece si la partícula se mueve en el sistema rotante).
    * **Fuerza Centrífuga:** $\vec{F}_{cf} = -m\,\vec{\omega} \times (\vec{\omega} \times \vec{r})$ (Depende únicamente de la posición radial respecto al eje de giro).
    """)

# ==========================================
# PESTAÑA 2: PRÁCTICA GUIADA (TRABAJO DEL ALUMNO)
# ==========================================
with tab2:
    st.header("Práctica de Laboratorio: El problema de los Puntos de Lagrange")
    st.write("**Objetivo:** Derivar la formulación matemática de los puntos de equilibrio en el sistema Tierra-Luna resolviendo el problema en coordenadas polares.")
    
    st.subheader("Condición de Equilibrio Estacionario")
    st.write("Para que existan puntos de equilibrio estacionarios en el sistema rotante, la velocidad y aceleración relativas deben ser nulas:")
    st.latex(r"\vec{v}_{rel} = 0, \quad \vec{a}_{rel} = 0 \implies \vec{F}_{grav} + \vec{F}_{cf} = 0")
    
    st.write("Este sistema dinámico puede describirse mediante extremos de un **Potencial Efectivo ($U_{eff}$)**:")
    st.latex(r"U_{eff} = - \frac{GM_T}{r_T} - \frac{GM_L}{r_L} - \frac{1}{2}\omega^2 r^2 \quad \implies \quad \nabla U_{eff} = 0")

    st.markdown("---")
    st.subheader("✏️ Tu turno: Estación de Trabajo Autónomo")
    st.write("Utiliza las pistas teóricas y las constantes del problema para resolver las preguntas en tu hoja e ingresar las respuestas:")
    
    # Datos expuestos
    # ASÍ DEBE QUEDAR TU BLOQUE DE DATOS EN EL ARCHIVO:
    st.markdown(r"""
    **Datos del Sistema Tierra-Luna:**
    * $M_T = 5.97 \times 10^{24}\text{ kg}$
    * $M_L = 7.35 \times 10^{22}\text{ kg}$
    * $R = 3.84 \times 10^{8}\text{ m}$
    """)
    
    st.write(f"Velocidad angular calculada ($\omega$): **{omega:.4e} rad/s**")

    
    st.markdown("**Desafío 1: Puntos Triangulares ($L_4$ y $L_5$)**")
    st.write("Sabiendo que $L_4$ y $L_5$ forman un triángulo equilátero perfecto con la Tierra y la Luna, ¿cuál es la distancia exacta (en metros) desde el centro de la Tierra hasta el punto $L_4$?")
    
    resp_l4 = st.number_input("Distancia Tierra - L4 (m):", min_value=0.0, format="%.2e", key="l4_input")
    if st.button("🚀 Verificar Geometría de L4"):
        if np.isclose(resp_l4, R, rtol=1e-3):
            st.success(f"¡Excelente! Al ser un triángulo equilátero, la distancia a la Tierra es exactamente igual al radio orbital $R = {R:.2e}\text{ m}$.")
        else:
            st.error("Respuesta incorrecta. Revisa las propiedades de distancias en polares para un triángulo de lados iguales.")

    st.markdown("**Desafío 2: Localización Numérica del Punto Colineal $L_1$**")
    st.write("En la línea recta que une ambos astros ($\theta = 0$), el equilibrio de la fuerza gravitatoria neta y la centrífuga se reduce a la ecuación polinómica de quinto grado:")
    st.latex(r"-\frac{GM_T}{r^2} + \frac{GM_L}{(R-r)^2} + \omega^2 r = 0")
    st.write("Resuelve esta ecuación en tu calculadora para hallar el radio $r$ desde el centro de la Tierra hasta $L_1$:")
    
    resp_l1 = st.number_input("Radio r de L1 (m):", min_value=0.0, format="%.3e", key="l1_input")
    r_l1_teorico = 3.26e8
    
    if st.button("🚀 Verificar Cálculo de L1"):
        if np.isclose(resp_l1, r_l1_teorico, rtol=1e-2):
            st.balloons()
            st.success(f"🎉 ¡Espectacular! El punto $L_1$ se localiza exactamente a {r_l1_teorico:.2e} m de la Tierra. ¡Has validado analíticamente tu cálculo!")
        else:
            st.error("El valor numérico no satisface el equilibrio de fuerzas. Revisa tus despejes y aproximaciones.")

# ==========================================
# PESTAÑA 3: LABORATORIO VIRTUAL (MAPA)
# ==========================================


with tab3:
    st.header("Visualización de la Topografía del Potencial")
    st.write("Comprueba tus cálculos analíticos interactuando con el mapa del potencial efectivo del sistema síncrono.")
    
    if st.checkbox("🗺️ Activar Mapa de Contornos Gravitatorios"):
        with st.spinner("Calculando superficies de energía..."):
            # Generación de la grilla espacial
            x_vals = np.linspace(-R*1.5, R*1.5, 200)
            y_vals = np.linspace(-R*1.5, R*1.5, 200)
            X, Y = np.meshgrid(x_vals, y_vals)
            
            # Distancias y Baricentro
            r_T = np.sqrt(X**2 + Y**2)
            r_L = np.sqrt((X - R)**2 + Y**2)
            x_b = R * (M_L / (M_T + M_L))
            r_bar_sq = (X - x_b)**2 + Y**2
            
            # Ecuación del Potencial (Evitando singularidades en los centros infinitos)
            U = - (G * M_T / (r_T + 1e6)) - (G * M_L / (r_L + 1e6)) - 0.5 * (omega**2) * r_bar_sq
            U_clipped = np.clip(U, -2e6, 0)
            
            # Gráfico interactivo con Plotly
            fig = go.Figure(data=go.Contour(
                z=U_clipped, x=x_vals, y=y_vals,
                colorscale='Viridis',
                contours_start=-1.6e6, contours_end=-1.1e6, contours_size=20000,
                colorbar=dict(title="U_eff (J/kg)")
            ))
            
            # --- CORREGIDO AQUÍ: Se añadieron las listas de coordenadas numéricas [0] ---
            fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers+text', text=["Tierra"], textposition="top center", marker=dict(color='blue', size=14), name="Tierra"))
            fig.add_trace(go.Scatter(x=[R], y=[0], mode='markers+text', text=["Luna"], textposition="top center", marker=dict(color='orange', size=9), name="Luna"))
            
            # Ubicación exacta de las soluciones del gradiente
            fig.add_trace(go.Scatter(x=[3.26e8, 4.49e8, -3.81e8], y=[0, 0, 0], mode='markers', marker=dict(color='red', symbol='x', size=11), name="Puntos Colineales (L1, L2, L3)"))
            fig.add_trace(go.Scatter(x=[R*0.5, R*0.5], y=[R*np.sin(np.pi/3), -R*np.sin(np.pi/3)], mode='markers', marker=dict(color='cyan', symbol='diamond', size=11), name="Puntos Triangulares (L4, L5)"))

            fig.update_layout(
                xaxis_title="Eje X (m)", yaxis_title="Eje Y (m)",
                width=850, height=700,
                legend=dict(yanchor="top", y=0.98, xanchor="left", x=0.02)
            )
            st.plotly_chart(fig, use_container_width=True)

    st.subheader("💬 Conclusiones para el Reporte de Laboratorio")
    st.markdown("""
    * **Puntos Colineales:** Corresponden matemáticamente a puntos de silla de montar (estabilidad condicional).
    * **Puntos Triangulares:** Actúan como máximos locales del potencial en el plano rotante. Debido al efecto estabilizador de la **Fuerza de Coriolis** (cuando la partícula adquiere velocidad relativa), estos puntos atrapan polvo cósmico y satélites de forma natural.
    """)
