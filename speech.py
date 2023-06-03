import speech_recognition as sr

class Speech:
    def __init__(self) -> None:
        pass
    
    def recognize():
        print('Detecting speech...')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            print('Loading Whisper model...')
            message = r.recognize_whisper(audio)
            print('Finish!')
            return message

        except sr.UnknownValueError:
            print('Finish!')
            return