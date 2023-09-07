import streamlit as st
from maps import display_map
from chatbot import chatbot

# Habilitar acceso al micrófono y altavoces
st.set_option('deprecation.showfileUploaderEncoding', False)

# Llamar a las funciones
display_map()
chatbot()
