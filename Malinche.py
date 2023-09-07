import streamlit as st
from maps import display_map
from chatbot import chatbot
from google_images import buscar_imagenes
from config import google_api_key, google_cse_id  # Asegúrate de importar las claves necesarias

from PIL import Image

imagen1 = Image.open("resources/TrenMaya.png")
imagen1 = imagen1.resize((210, 340))
imagen2 = Image.open("resources/logomalin.png")
imagen2 = imagen2.resize((203, 183))
imagen3 = Image.open("resources/logo_letras.png")
imagen4 = Image.open("resources/trenmaya1.png")

col1, col2, col3,col4= st.columns([2,2,6,5])

with col2:
    st.image(imagen1)

with col3:
    st.write(display_map())

with col2:
    st.image(imagen2)

with col4:
    prompt = "Hola"  # Define el prompt que deseas utilizar
    images = chatbot(prompt, google_api_key, google_cse_id)
    if images:
        col2.write("Imágenes encontradas:")
        for image in images:
            col2.image(image['link'], caption=image['title'], use_column_width=True)
