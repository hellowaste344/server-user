import whisper

# tiny | base | small | medium
model = whisper.load_model("base")

transcription = model.transcribe("test.mp3")

print(transcription["text"])
