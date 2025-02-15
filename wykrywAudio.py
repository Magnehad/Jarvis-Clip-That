import speech_recognition as sr 
from faster_whisper import WhisperModel
model_size = "large-v3"
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# obtain audio from the microphone
def mow():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Sluchanie...")
            
            try:
                audio = r.listen(source,2,6)
                try:
                    print("Uslyszany tekst: " + r.recognize_whisper(audio, language="english"))
                    tekst = r.recognize_whisper(audio, language="english")
                except sr.UnknownValueError:
                    print("Whisper could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Whisper; {e}")
                if tekst !=" ":
                    return tekst
            except sr.WaitTimeoutError:
                pass
        
        
def google(tekst):
    a=0
    lista=tekst.split()
    dlugosc=len(lista)
    for x in lista:
        a=a+1
        if x =="Google" or x=="google" or x=="Google," or x =="google,":
            for i in range(a):
                del lista[0]
            
    return ' '.join(lista)

