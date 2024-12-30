import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui  # pip install pyautogui


# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Select a female voice


def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Please tell me, what can I do for you?")


def takeCommand():
    """Take microphone input from the user and return it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}\n")
        except Exception as e:
            print("Error:", e)
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return "none"
        return query.lower()


if __name__ == '__main__':
    while True:
        query = takeCommand()

        if 'wake up' in query:
            wishMe()

            while True:
                query = takeCommand()

                if 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'microsoft edge' in query:
                    speak("Opening Microsoft Edge...")
                    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

                elif 'brave' in query:
                    speak("Opening Brave Browser...")
                    os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

                elif 'search' in query or 'open' in query:
                    query = query.replace("search", "").replace("open", "").strip()
                    pywhatkit.search(query)
                    speak(f"Here are the results for {query}")

                elif 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia", "").strip()
                    try:
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    except Exception:
                        speak("Sorry, no results found.")

                elif 'play' in query:
                    song = query.replace("play", "").strip()
                    speak(f"Playing {song} on YouTube")
                    pywhatkit.playonyt(song)

                elif 'type' in query:
                    speak("What should I type?")
                    while True:
                        text_to_type = takeCommand()
                        if "exit typing" in text_to_type:
                            speak("Exiting typing mode.")
                            break
                        pyautogui.write(text_to_type)

                elif 'exit' in query:
                    speak("It was a pleasure assisting you. Goodbye!")
                    quit()

                elif 'break' in query:
                    speak("Taking a break. Let me know when you need me.")
                    break

                elif 'how are you' in query:
                    speak("I'm doing well, thank you for asking! How can I assist you today?")

                elif 'who are you' in query:
                    speak("I'm Jarvis, your virtual assistant, created using Python.")

                elif 'what is your name' in query:
                    speak("My name is Jarvis. How can I assist you today?")

                elif 'thank you' in query or 'good job' in query:
                    speak("You're welcome! I'm here to help.")

        else:
            print("I'm sleeping. Say 'wake up' to activate me.")
