import pyttsx3
import speech_recognition as sr
import eel
def speak(text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',170)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=10,phrase_time_limit=6)
  
    try:
        print('recognizing...')
        quary=r.recognize_google(audio.language='en')
        print(f'user said:{query}')

    except Exception as e:
        return""
    
    return quary.lower()

text= takecommand()
speak(text)