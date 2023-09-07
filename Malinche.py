import streamlit as st
from maps import display_map
from chatbot import chatbot
from google_images import buscar_imagenes
from config import google_api_key, google_cse_id  # Asegúrate de importar las claves necesarias

from PIL import Image

imagen1 = Image.open("resources/TrenMaya.png")
imagen2 = Image.open("resources/logomalin.png")
imagen3 = Image.open("resources/logo_letras.png")
imagen4 = Image.open("resources/trenmaya1.png")

col1, col2, col3= st.columns([1,4,5])

with col1:
    st.image(imagen1)

with col2:
    st.write(display_map())

with col3:
    st.image(imagen2)

with col3:
    prompt = "Hola"  # Define el prompt que deseas utilizar
    images = chatbot(prompt, google_api_key, google_cse_id)

if images:
    st.write("Imágenes encontradas:")
    for image in images:
        st.image(image['link'], caption=image['title'], use_column_width=True)
