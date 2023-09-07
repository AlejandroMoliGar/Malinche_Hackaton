import openai
import pyttsx3
import streamlit as st
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()
recognizer = sr.Recognizer()

st.title("Chatbot con voz")

if st.button("Habilitar Reconocimiento de Voz"):
    st.write("Habla ahora...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Ajusta para ruido ambiente
        audio = recognizer.listen(source, timeout=5)
        st.write("Escuchado, procesando...")

    try:
        prompt = recognizer.recognize_google(audio, language="es-ES")
        st.write("Pregunta (Reconocimiento de Voz):", prompt)

        if prompt.lower() == "exit":
            st.write("Saliendo del programa...")
        elif prompt.strip():
            try:
                completion = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=2048
                )

                response_text = completion.choices[0].text
                st.write("Respuesta:", response_text)
                engine.say(response_text)
                engine.runAndWait()
            except Exception as e:
                st.write("Error al obtener una respuesta:", str(e))
        else:
            st.write("El reconocimiento de voz no capturó texto válido.")

    except sr.UnknownValueError:
        st.write("No se pudo entender el audio. ¿Puedes repetir la pregunta?")
    except sr.RequestError as e:
        st.write("Error en la solicitud de reconocimiento de voz:", str(e))
