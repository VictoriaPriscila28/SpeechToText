import speech_recognition as sr

# função para ouvir e reconhecer a fala
def ouvir_microfone():
# habilita o microfone do usuario
    microfone = sr.Recognizer()

# usando o microfone
    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print("diga algo:")
        audio = microfone.listen(source)

    try:

        frase = microfone.recognize_google(audio,language='pt-BR')
        print("voce disse:"+frase)

    except sr.UnknownValueError:

        print("nao entendi")

    return frase

ouvir_microfone()




