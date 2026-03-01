import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say sth\n")
    audio_text = r.listen(source)
    print("thanks")

    try:
        print("text: ", r.recognize_google(audio_text))
    except:
        print("Sorry, I did not get that")
