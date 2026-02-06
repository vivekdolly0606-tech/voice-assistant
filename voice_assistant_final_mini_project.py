import time
import webbrowser
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import traceback

# --------- Initialize engine once (global) ----------
engine = pyttsx3.init()
engine.setProperty("rate", 230)
engine.setProperty("volume", 1.0)

def talk(text):
    """Speak text and also print debug info."""
    try:
        print("TALK:", text)               # debug: confirm we reached talk()
        engine.say(text)
        engine.runAndWait()                # blocking: wait until speech finishes
        print("TALK finished")             # debug: confirm finishing
    except Exception as e:
        print("TTS error:", e)
        traceback.print_exc()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (adjusting for ambient noise)")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source, phrase_time_limit=6)
    try:
        cmd = r.recognize_google(audio).lower()
        print("You said:", cmd)
        return cmd
    except sr.UnknownValueError:
        print("Could not understand audio")
        talk("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Speech service error:", e)
        talk("Sorry, my speech service is down.")
        return ""

# --- MAIN LOOP (replace your existing loop with this) ---
talk("Hello vivek, I am your smart assistant. How can I help you?")

while True:
    command = listen()

    if not command:
        continue

    # simple debug for command reaching
    print("Handling command:", command)

    if "hello" in command:
        talk("Hello! How are you?")

    elif "your name" in command:
        talk("I am your assistant, created by Mudhu.")

    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        talk(f"The time is {now}")

    elif "youtube" in command:
        # Make sure we speak first and allow a tiny pause before opening the browser
        talk("Opening YouTube for you.")
        time.sleep(0.5)
        try:
            webbrowser.open("https://www.youtube.com")
            print("Opened YouTube")
        except Exception as e:
            print("Error opening browser:", e)
            traceback.print_exc()

    elif "google" in command:
        talk("Opening Google.")
        time.sleep(0.4)
        webbrowser.open("https://www.google.com")
          

    elif "tell me some joke" in command:
        import pyjokes
        talk(pyjokes.get_joke())

    elif "play music" in command:
        music_folder = "C:/Users/Public/Music"  # change path if needed
        import os, random
        try:
            songs = os.listdir(music_folder)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_folder, song))
                talk("Playing music for you.")
            else:
                talk("No music files found in your music folder.")
        except Exception as e:
            print("Music error:", e)
            traceback.print_exc()
            talk("Sorry, I could not play music.")
    elif "whatsapp" in command:
        talk("Opening WhatsApp.")
        time.sleep(0.4)
        webbrowser.open("https://www.whatsapp.com")
    elif "netflix" in command:
        talk("Opening Netflix.")
        time.sleep(0.4)
        webbrowser.open("https://www.netflix.com")
    elif "hotstar" in command:
        talk("Opening Hotstar.")
        time.sleep(0.4)
        webbrowser.open("https://www.hotstar.com")
    elif "youtube" in command:
        talk("Opening YouTube.")
        time.sleep(0.4)
        webbrowser.open("https://www.youtube.com")
    elif "google" in command:
        talk("Opening Google.")
        time.sleep(0.4)
        webbrowser.open("https://www.google.com")
    elif "instagram" in command:
        talk("Opening Instagram.")
        time.sleep(0.4)
        webbrowser.open("https://www.instagram.com")
    elif "facebook" in command:
        talk("Opening Facebook.")
        time.sleep(0.4)
        webbrowser.open("https://www.facebook.com")
    elif "twitter" in command:
        talk("Opening Twitter.")
        time.sleep(0.4)
        webbrowser.open("https://www.twitter.com")
    elif "linkedin" in command:
        talk("Opening LinkedIn.")
        time.sleep(0.4)
        webbrowser.open("https://www.linkedin.com")
    elif "amazon" in command:
        talk("Opening Amazon.")
        time.sleep(0.4)
        webbrowser.open("https://www.amazon.in")
    elif "flipkart" in command:
        talk("Opening Flipkart.")
        time.sleep(0.4)
        webbrowser.open("https://www.flipkart.com")
    elif "prime" in command:
        talk("Opening Amazon Prime Video.")
        time.sleep(0.4)
        webbrowser.open("https://www.primevideo.com")
    elif "spotify" in command:
        talk("Opening Spotify.")
        time.sleep(0.4)
        webbrowser.open("https://www.spotify.com")
    elif "gmail" in command:
        talk("Opening Gmail.")
        time.sleep(0.4)
        webbrowser.open("https://mail.google.com")
    elif "maps" in command:
        talk("Opening Google Maps.")
        time.sleep(0.4)
        webbrowser.open("https://maps.google.com")
    elif "stop" in command or "exit" in command:
        talk("Goodbye Mudhu! See you soon.")
        break

    else:
        # debug: tell exactly what we will speak
        print("Fallback speak:", command)
        talk("I heard you say " + command)
