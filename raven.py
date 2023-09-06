import speech_recognition as sr
import  pyttsx3, pywhatkit

name= "Mario"
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

def talk(some_text):
    engine.say(some_text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print ("Te Estoy escuchando Cuervo..")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc,language= "es")
            rec = rec.lower()
    except sr.UnknownValueError:
        print("dilo de nuevo Cuervo!")
    return rec
def run_Mario():
    while True:
        try:
            rec = listen()
            print(rec)
        except UnboundLocalError:
            talk("dilo de nuevo Cuervo!")
            continue
        if name in rec:
            rec = rec.replace(name, '').strip()
            if 'reproduce' in rec:
                song = rec.replace('reproduce', '').strip()
                pywhatkit.playonyt(song)
                talk(f"Reproduciendo {song}.")
if __name__ == '__main__':
    run_Mario()