import speech_recognition as sr
import webbrowser as web

def main():
    path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("por favor diga algo:")
        audio = r.listen(source)
        print("reconhecendo...")

    try:
        dest = r.recognize_google(audio, language='pt-BR')
        print("voce disse:" + dest)

        web.open("https://" + dest)

    except Exception as e:
        print("nao entendi" + str(e))


if __name__ == "__main__":
    main()