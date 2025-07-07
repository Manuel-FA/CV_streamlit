import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Currículum Vitae", layout="wide")

# Sidebar de navegación
st.sidebar.title("Navegación")
seccion = st.sidebar.radio("📂 Secciones:", [
    "📋 Perfil profesional", 
    "💼 Experiencia",
    "🛠️ Habilidades",
    "🎓 Estudios Universitarios", 
    "📚 Cursos y Certificaciones"
])

# Funciones para cada sección
def mostrar_perfil():
    import streamlit as st

    st.markdown(
        "<h1 style='text-align: center;'>👋 Hola, soy Manuel Alberto Flores Alfaro</h1>",
        unsafe_allow_html=True
    )
    st.markdown("<h4 style='text-align: center;'>Analista de Datos | Científico de Datos</h4>", unsafe_allow_html=True)
    
    st.markdown("""
    Soy un ingeniero especializado en análisis de datos y programación. Transformo datos utilizando herramientas como Excel y Python, proporcionando información clave para la toma de decisiones estratégicas.
    """)

    st.markdown("Proyectos destacados:")

    st.markdown("""
    **📊 Aplicación web para análisis de datos**  
    Desarrollé una aplicación web para el análisis de información de ventas utilizando Python y Streamlit, útil para mostrar dashboards en la Web. Actualmente, el proyecto se encuentra en proceso de escalamiento con Plotly Dash y Flask, con el objetivo de convertirlo en un sistema centralizado que permita a distintos niveles de usuarios consultar datos clave: desde análisis diarios de ventas hasta resultados generados por algoritmos de machine learning.
    
    Puedes explorar Plotly en el siguiente enlace: https://plotly.com/

    """)

    st.markdown("""
    **🧠 Publicación de un artículo científico**  
    Obtuve una beca por parte del CONACYT (actualmente SECIHTI) para desarrollar un proyecto de investigación en maestría en la UV, con asesoramiento por parte de personal del INIDETAM. Desarrollé un algoritmo de inteligencia artificial en MATLAB con técnicas de algoritmos genéticos para optimizar el diseño aerodinámico de drones. Se obtuvo un artículo científico, el cual fue publicado en la editorial *Multidisciplinary Digital Publishing Institute*.

    Visita la publicación en el siguiente enlace: https://doi.org/10.3390/aerospace11010044
    """)

    st.image("imagenes/portada_articulo_alta_res.png", width=1200)

def mostrar_experiencia():
    st.title("💼 Experiencia")
    st.markdown("""
**Analista administrativo**  
*World Korei Corporation*  
*Noviembre 2023 - Presente*

- En desarrollo de un proyecto de recomendación de artículos con TensorFlow para utilizarlo en un sistema B2B. De la misma forma que empresas como Netflix o Amazon recomiendan artículos según los gustos de sus clientes, se está obteniendo con TensorFlow Recommenders un listado por artículo de qué otros artículos tienen una alta probabilidad de ser comprados, esto de acuerdo a la constancia con que aparecen en la misma factura.  
- Predicciones de rotación de stock con el algoritmo de machine learning Prophet, para determinar los máximos y mínimos de stock por almacén.  
- Segmentación de clientes con k-means para agrupar los clientes de acuerdo con la venta, considerando el número de facturas, el número de artículos que representan el 80% de su venta y el costo de venta.  
- Creación de dashboards de ventas con Python y Streamlit para la visualización interactiva de datos. Actualmente se utiliza para obtener análisis de clientes que antiguamente tardaban más de 2 horas en realizarse, ahora solo lleva 10 minutos.
- Automatización de reportes con Access mediante consultas SQL.  
- Análisis de ventas de maquinaria en Excel para optimizar la toma de decisiones directivas, evaluando el desempeño de vendedores, clientes y productos.  
- Seguimiento de procesos con proveedores y el equipo de ventas.  

---

**Analista de datos Freelancer**  
*Mediterranean Shipping Company*  
*Octubre 2023 - Presente*

- Elaboración de reportes trimestrales de mercancía transportada, utilizando gráficos en Excel para una interpretación más eficiente. Este es un trabajo esporádico, en donde el jefe de la oficina solicita mi consultoría para el análisis de datos.

---

**Profesor**  
*Computación del Golfo*  
*Junio 2023 - Febrero 2024*

- Capacitar a jóvenes hasta adultos mayores, de forma personalizada y en grupo, en el uso de Excel básico, funciones, tablas dinámicas, dashboards y macros.  
- Impartir clases de Inglés A1.
""")

def mostrar_habilidades():
    st.title("🛠️ Habilidades")

    st.markdown("# Lenguaje de programación (Python)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Manipulación de datos")
        st.markdown("- Pandas")
        st.markdown("- NumPy")
        st.markdown("### Visualización de datos")
        st.markdown("- Plotly")
        st.markdown("- Seaborn")
        st.markdown("- Matplotlib")
    with col2:
        st.markdown("### Machine Learning")
        st.markdown("- Scikit-learn")
        st.markdown("- TensorFlow")
        st.markdown("### Desarrollo de aplicaciones web")
        st.markdown("- Dash")        
        st.markdown("- Streamlit")

    st.markdown("# Softwares para análisis de datos")
    st.markdown("- Excel")
    st.markdown("- Acces")
    st.markdown("- MATLAB")

    st.markdown("# Softwares empresariales")
    st.markdown("- SAP")    
    st.markdown("- Odoo")

    st.markdown("# Herramientas exploradas que busco aplicar con mayor frecuencia")
    st.markdown("- Power BI")
    st.markdown("- SQL")

def mostrar_educacion():
    st.title("🎓 Estudios Universitarios")
    st.markdown("""
**Maestría en Ingeniería Aplicada**  
*Universidad Veracruzana*  
*Febrero 2020 - Noviembre 2022*
            
- Análisis de resultados de experimentaciones y presentación de informes.
- Programación de inteligencia artificial con técnicas avanzadas de algoritmos genéticos en MATLAB.
- Publicación de un artículo científico en la editorial *Multidisciplinary Digital Publishing Institute*. Respaldado por CONACYT.
- Uso de Ubuntu para la utilización de OpenFOAM, un programa para análisis de fluidos.
            
**Ingeniería Mecánica**  
*Universidad Veracruzana*  
*Agosto 2014 - Julio 2019*
            
El éxito de mi trabajo recepcional, en el cual utilicé un algoritmo de IA para optimizar la aerodinámica de un diseño de drones, me permitió presentar ponencias en los siguientes espacios:
- Congreso Internacional de Investigación de Academia Journals Puebla 2019.
- VII Simposio Mexicano de Vehículos Aéreos no Tripulados del Instituto de Investigación y Desarrollo Tecnológico de la Armada de México.
    """)

    col1, col2 = st.columns(2)
    with col1:
            st.image("imagenes/puebla.PNG", width=400)
    with col2:
            st.image("imagenes/inidetam.PNG", width=400)

def mostrar_cursos():
    st.title("📚 Cursos y Certificaciones")

    st.markdown("### 📗 Cursos completados")
    
    st.markdown("""
- IBM Machine Learning. Coursera. Junio 2025.
    """)
    st.image("imagenes/ml.png", width=800)

    st.markdown("""
- IBM Data Analyst Professional Certificate. Coursera. Mayo 2024.
    """)
    st.image("imagenes/data_analyst.png", width=800)

    st.markdown("""             
- Microsoft Power BI Data Analyst. Coursera. Julio 2024.
    """)
    st.image("imagenes/bi.png", width=800)
    
    st.markdown("""
- Comunicación para líderes. Platzi. Junio 2024.
    """)

    st.markdown("### 📘 Cursos en proceso")
    st.markdown("""
- Data Engineer. Platzi.
- Fundamentos de Finanzas Personales y Corporativas. Platzi.
- Inglés Intermedio B1. Platzi.
    """)

    st.markdown("### 🎯 Educación a futuro")
    st.markdown("""
- Primer paso: Escuelas de análisis de datos, programación, finanzas y habilidades blandas en Platzi.
- Segundo paso: Múltiples cursos de ciencias de datos y finanzas en Coursera.
- Tercer paso: Maestría en Ciencia de Datos con enfoque en soluciones empresariales.
    """)


# Mostrar la sección seleccionada
if seccion == "📋 Perfil profesional":
    mostrar_perfil()
elif seccion == "💼 Experiencia":
    mostrar_experiencia()
elif seccion == "🛠️ Habilidades":
    mostrar_habilidades()
elif seccion == "🎓 Estudios Universitarios":
    mostrar_educacion()
elif seccion == "📚 Cursos y Certificaciones":
    mostrar_cursos()
