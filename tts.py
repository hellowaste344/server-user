import pyttsx3

engine = pyttsx3.init()

# VOICE
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # index 0 male 1 female

engine.say("Hi, I am Samantha")
engine.runAndWait()

pyttsx3.speak("Your AI agent")

# RATE
engine.setProperty("rate", 140)
rate = engine.getProperty("rate")
print(rate)


# VOLUME
engine.setProperty("volume", 2)
volume = engine.getProperty("volume")
print(volume)

engine.say("My current volume is" + str(volume))

engine.runAndWait()

engine.stop()

engine.save_to_file(
    "Welcome to My Darkness",
    "test.mp3",
)

engine.runAndWait()
