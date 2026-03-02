import pyttsx3

engine = pyttsx3.init()

# VOICE
voices = engine.getProperty("voices")
for index, voice in enumerate(voices):
    print(f"Index {index}")
    print(f"Name {voice.name}")
    print(f"ID {voice.id}")
    print(f"Gender {voice.gender}")
    print("*" * 10)

engine.setProperty("voice", voices)

engine.say("Hi, I am Samantha")
engine.runAndWait()

pyttsx3.speak("Your AI agent")

# RATE
engine.setProperty("rate", 140)
rate = engine.getProperty("rate")
print(rate)


# VOLUME
engine.setProperty("volume", 1)
volume = engine.getProperty("volume")
print(volume)

engine.say("My current volume is" + str(volume))

engine.runAndWait()

engine.stop()

engine.save_to_file(
    "Super Computers Can Change The World",
    "test.mp3",
)

engine.runAndWait()
