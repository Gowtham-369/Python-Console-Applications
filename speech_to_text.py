import speech_recognition as sr
AUDIO_FILE = ("Manyampuli.wav")
#use AUDIO_FILE as source
r = sr.Recognizer() #initialise the recognizer
with sr.AudioFile(AUDIO_FILE) as source: #recogniser identifies the source
    audio = r.record(source) #reads the source
#records the audio file inputed
try:
    print("audiofile contains :",r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from google Speech Recognition")
    


