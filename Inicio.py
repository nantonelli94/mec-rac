import streamlit as st
import os
from pathlib import Path

# 1. Configuración global de la plataforma educativa
st.set_page_config(
    page_title="Manual de Mecánica Teórica",
    page_icon="📚",
    layout="wide"
)

# Portada principal
st.title("📚 Manual Moderno de Mecánica Teórica")
st.subheader("Un enfoque interactivo con simulaciones y ejercicios resueltos")
st.write("---")

# Introducción pedagógica
st.write("""
¡Bienvenido! Este manual interactivo está diseñado para estudiantes de física e ingeniería que buscan 
comprender los principios de la mecánica clásica mediante simulaciones dinámicas y resoluciones analíticas.
""")

st.info("👈 **Cómo usar este libro:** Utiliza la barra lateral de la izquierda para navegar o selecciona un módulo directamente desde el índice dinámico de abajo.")

# =========================================================
# 🛠️ SISTEMA DE ÍNDICE DINÁMICO (LECTURA AUTOMÁTICA)
# =========================================================
st.header("🗂️ Índice General del Curso")
st.write("Selecciona cualquier lección disponible para acceder a su contenido:")

# Definimos la ruta hacia tu carpeta de páginas
PAGES_DIR = Path(__file__).parent / "pages"

if PAGES_DIR.exists():
    # Escaneamos y filtramos solo los archivos que terminan en .py
    files = [f for f in os.listdir(PAGES_DIR) if f.endswith(".py")]
    
    # Los ordenamos alfabética o numéricamente (por eso tus prefijos '1_', '2_' son ideales)
    files.sort()
    
    if files:
        # Generamos la lista interactiva dinámicamente
        for file in files:
            # 1. Obtenemos la ruta relativa que requiere Streamlit para los enlaces de página
            page_path = f"pages/{file}"
            
            # 2. Limpiamos estéticamente el nombre del archivo para mostrarlo en el índice
            # Ejemplo: "1_📐_Calculo_Vectorial.py" -> "📐 Calculo Vectorial"
            clean_name = file.replace(".py", "").replace("_", " ")
            
            # Si el archivo empieza con un número para orden (ej: "1 "), limpiamos solo el número inicial
            parts = clean_name.split(" ", 1)
            if len(parts) > 1 and parts[0].replace(".", "").isdigit():
                clean_name = parts[1]
            
            # 3. Dibujamos el enlace interactivo nativo en forma de lista
            st.page_link(page_path, label=clean_name, icon="🔹")
    else:
        st.warning("Aún no hay módulos disponibles en la carpeta de lecturas.")
else:
    st.error("No se encontró la carpeta 'pages'. Asegúrate de que su nombre esté en minúsculas en tu repositorio de GitHub.")

st.write("---")
st.caption("Desarrollado con ❤️ usando Inteligencia Artificial, Streamlit y GitHub.")
