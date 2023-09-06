import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()
recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Habla ahora...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Ajusta para ruido ambiente
        audio = recognizer.listen(source, timeout=5)

        print("Escuchado, procesando...")

    try:
        prompt = recognizer.recognize_google(audio, language="es-ES")
        print("Pregunta:", prompt)

        if prompt.lower() == "exit":
            break

        if prompt.strip():
            try:
                completion = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=2048
                )

                response_text = completion.choices[0].text
                print("Respuesta:", response_text)
                engine.say(response_text)
                engine.runAndWait()
            except Exception as e:
                print("Error al obtener una respuesta:", str(e))
        else:
            print("El prompt está vacío, por favor ingresa una pregunta válida.")

    except sr.UnknownValueError:
        print("No se pudo entender el audio. ¿Puedes repetir la pregunta?")
    except sr.RequestError as e:
        print("Error en la solicitud de reconocimiento de voz:", str(e))

print("Saliendo del programa...")
