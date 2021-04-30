import speech_recognition as sr
import time
from time import ctime
import webbrowser

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownVauleError:
            print('Hable bien wey')
        except sr.RequestError:
            print('Contrata un mejor internet che pobre')
        return voice_data
def respond(voice_data):
    if 'como te llamas' in voice_data:
        print('mi nombre es goku')
    if 'hora' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        buscar = record_audio('¿Qué necesitas buscar?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('Encontré esto: ' + buscar)
    if 'Lugar' in voice_data:
        lugar = record_audio("Donde we?")
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        print('Esto hay: ' + lugar)
    if 'color favorito' in voice_data:
        print('El guinda')
    if 'comida favorita' in voice_data:
        print('tus nalgas')

time.sleep(1)
print('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    print(voice_data)