import streamlit as st
from langdetect import detect
import speech_recognition as sr
from google_images import buscar_imagenes
import openai
from langdetect.lang_detect_exception import LangDetectException
from speech_recognition import WaitTimeoutError
import pyttsx3

# Variable global para el reconocedor de voz
recognizer = sr.Recognizer()

def chatbot(prompt, google_api_key, google_cse_id):
    st.title("Chatbot con voz")

    if st.button("Habilitar Reconocimiento de Voz"):
        st.write("Habla ahora...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = recognizer.listen(source, timeout=5)
            except WaitTimeoutError:
                st.error("El tiempo de espera se agotó. ¿Puedes repetir la pregunta?")
                return

            st.write("Escuchado, procesando...")

            try:
                detected_language = detect(recognizer.recognize_google(audio, language="es-MX"))
                
                if detected_language == "es":
                    prompt = recognizer.recognize_google(audio, language="es-MX")
                else:
                    prompt = recognizer.recognize_google(audio, language="en-US")

                st.write("Pregunta (Reconocimiento de Voz):", prompt)

                if prompt.lower() == "exit":
                    st.write("Saliendo del programa...")
                elif prompt.strip():
                    try:
                        completion = openai.Completion.create(
                            engine="text-davinci-003",
                            prompt=prompt,
                            max_tokens=1000
                        )

                        response_text = completion.choices[0].text
                        st.write("Respuesta:", response_text)

                        images = buscar_imagenes(prompt, google_api_key, google_cse_id)
                        if images:
                            num_images = len(images)
                            num_groups = num_images // 5 + (num_images % 5 > 0)
                            cols = st.columns(2)
                            for i in range(num_groups):
                                group_images = images[i*5 : (i+1)*5]
                                for image in group_images:
                                    cols[0].image(image['link'], caption=image['title'], use_column_width=True)

                        # Convertir respuesta a audio
                        engine = pyttsx3.init()
                        engine.say(response_text)
                        engine.runAndWait()
                        
                    except Exception as e:
                        st.write("Error al obtener una respuesta:", str(e))
            except LangDetectException as e:
                st.write("Error al detectar el idioma:", str(e))
            except sr.UnknownValueError:
                st.write("No se pudo entender el audio. ¿Puedes repetir la pregunta?")
            except sr.RequestError as e:
                st.write("Error en la solicitud de reconocimiento de voz:", str(e))

