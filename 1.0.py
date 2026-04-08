import speech_recognition as sr
import os
import time
from gtts import gTTS
from playsound import playsound

reconhecedor = sr.Recognizer()

def falar(texto):
    print("rex:", texto)
    tts = gTTS(text=texto, lang='pt-br')
    tts.save("voz.mp3")
    playsound("voz.mp3")
    os.remove("voz.mp3")

def ouvir_comando():
    with sr.Microphone() as source:
        print('fale:')
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = reconhecedor.listen(source, timeout=5)
            texto = reconhecedor.recognize_google(audio, language='pt-BR').lower()
            print("Você:", texto)
            return texto
        except:
            return ""

def responder(comando):
    if 'codigo' in comando or 'código' in comando:
        falar("Abrindo o Visual Studio")
        os.system('code')

    elif 'navegador' in comando or 'google' in comando:
        falar("Abrindo o navegador")
        os.system('chrome')

    elif 'hora' in comando:
        from datetime import datetime
        hora = datetime.now().strftime('%H:%M')
        falar("Agora são {hora}")
        
while True:
    comando = ouvir_comando()

    if 'rex' in comando:
        comando = comando.replace('rex', '').strip()
        falar("Olá, Senhor")
        responder(comando)

    time.sleep(1)
