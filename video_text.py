import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable
with sr.AudioFile(audio_file_path) as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text)
    print(text)
