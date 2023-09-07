import streamlit as st
from maps import display_map
from chatbot import chatbot
from google_images import buscar_imagenes
from config import google_api_key, google_cse_id

from PIL import Image
col1, col2, col3, col4 =st.columns([1,2,6,5])
imagen1 = Image.open("resources/TrenMaya.png")
imagen1 = imagen1.resize((210, 340))
imagen2 = Image.open("resources/logomalin.png")
imagen2 = imagen2.resize((203, 183))

# Definir contenedor para la primera fila
fila1 = st.container()

# Organizar elementos dentro de la primera fila
with fila1:
    with col2:
        st.image(imagen1, use_column_width=True)
    with col3:
        st.write(display_map())
    with col2:
        st.image(imagen2, use_column_width=True)

# Mostrar el chat y las imágenes generadas
prompt = "Hola"
with col4:
    images = chatbot(prompt, google_api_key, google_cse_id)
with fila1:
    if images is not None:
        st.write("Imágenes encontradas:")
        for image_data in images:
            st.image(image_data['link'], caption=image_data['title'], use_column_width=True)