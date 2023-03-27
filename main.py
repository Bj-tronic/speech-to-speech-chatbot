import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change the index to select a different voice


# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Define function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print('Listening...')
        speak('Listening')
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-US')
        print(query)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        print(f'User said: {query}\n')
    except Exception as e:
        print('Sorry, I did not understand that.')
        query = None
    return query


# Define function to process user queries
def process_query(query):
    if query is not None:
        if 'wikipedia' in query.lower():
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia...')
            speak(results)
        elif 'hi' in query.lower():
            speak('Hello, how are you?')
        elif 'time' in query.lower():
            now = datetime.datetime.now().strftime('%I:%M %p')
            speak(f'The time is {now}')
        else:
            speak('Sorry, I do not know how to do that.')


# Main loop
while True:
    query = recognize_speech()
    process_query(query)
