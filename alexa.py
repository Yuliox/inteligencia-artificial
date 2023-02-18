import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import subprocess

# name of the virtual assistant
name = 'alexa'
flag = 1

listener = sr.Recognizer()

# Configuracion de la voz de alexa
voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)
voice. setProperty('rate', 178)
voice.setProperty('volume', 0.7)

def talk(text):
    voice.say(text)
    voice.runAndWait()

def listen():

    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            comando = listener.recognize_google(voice, language='es-MX')
            comando = comando.lower()
            
            if name in comando:
                comando = comando.replace(name, '')
                flag = run(comando)
            else:
                talk("Vuelve a intentarlo, no reconozco: " + comando)
    except:
        pass
    return flag

def run(comando):

    if 'reproduce' in comando:
        music = comando.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'abre' in comando or 'abrir' in comando:
        sites={
            'google':'google.com',
            'youtube':'youtube.com',
            'instagram':'instagram.com'
            }
        for i in list(sites.keys()):
            if i in comando:
                subprocess.call(f'start chrome.exe {sites[i]}', shell=True)
                talk(f'Abriendo {i}')
    elif 'abre whatsapp' in comando:
        pywhatkit.open_web()
    elif 'hora' in comando:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in comando:
        order = comando.replace('busca', '')
        pywhatkit.search(order)
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'cancelar' in comando:
        flag = 0
        talk("...")
    else:
        talk("Vuelve a intentarlo, no reconozco: " + comando)
    return flag

while flag:
    flag = listen()