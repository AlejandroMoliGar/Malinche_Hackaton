import streamlit as st
from maps import display_map
from chatbot import chatbot, mostrar_imagenes
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

with col1:
    st.image(imagen2)

with col1:
    st.write(mostrar_imagenes())

with col3:
    st.write(chatbot())
