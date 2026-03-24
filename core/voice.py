import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_verse():
    """
    Listen from microphone and return recognized Arabic text.
    Allows longer phrases for full verse recitation.
    Returns the spoken string, or None if recognition failed.
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)
            result = recognizer.recognize_google(audio, language="ar-SA")
            return result
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None