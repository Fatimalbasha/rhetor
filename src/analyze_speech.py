from faster_whisper import WhisperModel

audio_path = "outputs/test/audio.wav"

print("Loading model: ")
model = WhisperModel("base", device="cpu", compute_type="int8")
# "base" --> is the model size
# "int8" --> uses lower-precision computation to reduce memory usage

# Start transcribing This returns a generator (segments) and some info
print("Transcribing: ")
segments, info = model.transcribe(audio_path, word_timestamps= True)
# word_timestamps=True --> tells Whisper to tag every word with a start and end time

print(f"Detected language: {info.language}")

full_text =""
for segment in segments:
    full_text += segment.text

print("--- Transcript ---")
print(full_text)



