import speech_recognition as sr
import time
from time import ctime
import webbrowser
import playsound 
import os
import random
from gtts import gTTS

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            alexa_speak('Hable bien wey')
        except sr.RequestError:
            alexa_speak('Contrata un mejor internet che pobre')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'como te llamas' in voice_data:
        alexa_speak('mi nombre es goku')
    if 'hora' in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        buscar = record_audio('¿Qué necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Encontré esto: ' + buscar)
    if 'Lugar' in voice_data:
        lugar = record_audio("Donde we?")
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Esto hay: ' + lugar)
    if 'color favorito' in voice_data:
        alexa_speak('El guinda')
    if 'comida favorita' in voice_data:
        alexa_speak('tus nalgas')

time.sleep(1)
alexa_speak('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    print(voice_data)