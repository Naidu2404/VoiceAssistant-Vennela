import time
import pywhatkit as pk
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import wikipedia as wiki
import os
import datetime as dt



listener = sr.Recognizer()

def speak(text):
    print('Speaking...')
    print('')
    tts = gTTS(text, lang='te')
    tts.save('audio.mp3')
    time.sleep(1)
    playsound('audio.mp3')
    os.remove('audio.mp3')

va_name = "వెన్నెల"

speak("హలో నాని , నేను వెన్నెల , నన్ను ఎం చేయమంటావ్ ?")

def takecommand(check):
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            print('')
            audio = listener.listen(source)
            if check:
                command = listener.recognize_google(audio, language="te")
                if va_name in command:
                    command = command.replace("వెన్నెల ", "")
                    # print(command)
                    # speak(command)
                else:
                    command=""
            else:
                command = listener.recognize_google(audio, language="en-US")
    except:
        print('Check your microphone')
    return command

while True:
    cmd = takecommand(True)
    if cmd != "":
        if "వెళ్లొచ్చు" in cmd:
            speak("సరే నాని! అవసరం ఐతే మల్లి పిలువు ")
            break
        if "టైమ్" in cmd:
            ct=dt.datetime.now().strftime("%I:%M %p")
            print(ct)
            print('')
            speak(ct)
        if "యూట్యూబ్" in cmd:
            speak("ఏ వీడియో ప్లే చెయ్యాలో చెప్పు నాని")
            cmd = takecommand(False)
            print(cmd)
            print('')
            pk.playonyt(cmd)
            speak("ఎంజాయ్ చెయ్ వీడియో ని. అవసరం ఐతే మల్లి పిలువు ")
            break
        if "గూగుల్" in cmd:
            speak("దేని గురించి సెర్చ్ చెయ్యాలి ")
            cmd = takecommand(False)
            print(cmd)
            print('')
            pk.search(cmd)
        if "ఎవరు" in cmd:
            cmd =cmd.replace(" ఎవరు", '')
            info = wiki.summary(cmd, 2)
            print(info)
            print('')
            speak(info)
    else:
        speak("నువ్వు ఎం చెప్పలేదు నాని")
input('press enter to close')