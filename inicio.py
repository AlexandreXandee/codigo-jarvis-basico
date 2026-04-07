import speech_recognition as sr
import os
import time

reconhecedor = sr.Recognizer()

def ouvir_comando():
    with sr.Microphone() as source:
        print('fale:')
        reconhecedor.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = reconhecedor.listen(source, timeout=5)
            texto = reconhecedor.recognize_google(audio, language='pt-BR').lower()
            print(texto)
            return texto
        except Exception as e:
            print("Repita", e)
            return ""

while True:
    comando = ouvir_comando()

    if 'codigo' in comando or 'código' in comando:
        os.system('code')
    elif 'navegador' in comando or 'google' in comando:
        os.system('chrome')
    time.sleep(1)
