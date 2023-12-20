from pathlib import Path
import streamlit as st 
from PIL import Image

#Configuraciones
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Sebastián Nicolás González Riveros - Resumee.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

#Caracteristicas
PAGE_TITLE = "CV Digital | Sebastián Nicolás González Riveros"
PAGE_ICON = ":wave:"
NAME = "Sebastián González"
DESCRIPTION = """
Junior Python Developer | Machine Learning, Web Development, Python Scripts, SQL and MySQL | Seeking Entry-Level Opportunity!
"""
EMAIL = "sebagr96@gmail.com"
SOCIAL_MEDIA ={
    "LinkedIn": "https://www.linkedin.com/in/sebasgz96/",
    "GitHub" : "https://github.com/sebagz96",
    "Instagram" : "https://www.instagram.com/sebasgonza"
}

PROJECTS = {
    "✅ Acute Lymphoblastic Leukemia Detection with VGG-19 Trained Model" : "https://github.com/sebagz96/vgg19-leukemia_detection",
    "✅ Expanding cards tutorial with HTML and CSS" : "https://github.com/sebagz96/expand-cards"
}

#Cargar CSS y archivos
with open(css_file) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    pdfByte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#Seccion de informacion
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "📋 Download Resumee",
        data = pdfByte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
    )
    st.write("📬 E-mail: ", EMAIL)

#Social Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#Experiencia
st.write("#")
st.subheader("Experiencia y Practicas")
st.write(
"""
- ✅ Proyecto Cinetoon enfocado a un software de administracion a un cine desarrollado con PHP 7 - Laravel - MySql
- ✅ Detección Automatizada de Leucemia Linfoblástica Aguda con el algoritmo VGG-19 previamente entrenado
- ✅ Expanding Cards con HTML - CSS
"""
)

#skills
st.write("#")
st.subheader("Habilidades")
st.write(
"""
- Programación: Python (scikit-learn, tensorflow, keras)
- Manipulación de datos: Pandas, Numpy
- Modelado: Regresión Logistica, Support Vector Machine, Random Forest, Naive Bayes, Convolutional Neural Networks
- Databases: MySQL, sqlite3, Postgres

"""
)

#Proyectos
st.write("#")
st.subheader("Proyectos")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")