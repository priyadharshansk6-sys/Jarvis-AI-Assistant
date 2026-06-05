import speech_recognition as sr

def wait_for_wake_word():
    r = sr.Recognizer()
    r.energy_threshold = 100
    r.dynamic_energy_threshold = False
    print("Say 'Jarvis' to activate...")
    
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
                text = r.recognize_google(audio).lower()
                print(f"Heard: {text}")
                if "jarvis" in text:
                    print("✅ Wake word detected!")
                    return
            except sr.WaitTimeoutError:
                print("Listening...")
            except sr.UnknownValueError:
                print("Couldn't understand")
            except sr.RequestError:
                print("❌ No internet!")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    wait_for_wake_word()
    print("JARVIS activated!")