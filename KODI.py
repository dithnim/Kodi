import speech_recognition as sr
from functions import os_ops
import os
import random
import openai
import pyscreenshot as ImageGrab
import string
import pyttsx3 as tts

code = 0
engine = tts.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)


chat_gpt_api = "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" #Enter your api key here
openai.api_key = chat_gpt_api

def task_list(command):
    if command in ["calc","calculator","open calc","open calculator"]:
        speak("Opening the system calculator")
        os_ops.open_calculator()

    elif command in ["chrome","open google chrome","open google","google"]:
        speak("opening. google chrome")
        os_ops.open_chrome()

    elif command == 'vscode':
        speak("Opening vs code. Happy coding!")
        os_ops.open_vscode()

    elif command == 'edge':
        speak("Openning microsoft egde")
        os_ops.open_edge()

    elif command == 'cmd':
        speak("Openning windows command prompt")
        os_ops.open_cmd()

    elif command == 'screenshot':
        strt = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        img = ImageGrab.grab()
        img.save(f"screenshots\\{strt}.jpg")
        speak("Screenshot saved. Openning now")
        img.show()

    elif command == 'shutdown':
        speak("are you sure.")
        if (take_user_input() == 'yes'):
            speak("attempting system shutdown")
            os.system("shutdown /s")
        else:
            speak("aborting system shutdown")



def get_gpt(prompt):
        try:
                response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role':'user','content':prompt}
                ]
            )
                res = response['choices'][0]['message']['content']
        except:
            res = "Sorry, Servers are unreachable at the moment"
        return res


def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetuser():
    val = get_gpt(f"Your name is kodi and your purpose is to be Dineth's AI assistant and tell the user to say your name to activate")
    print('\n'+val)
    speak(val)


def take_user_input():
    global r;global audio;global code
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Processing...\n')
        query = r.recognize_google(audio)
        print("You said:",query)
        query = query.lower()

        if not query in ['exit','stop','goodbye','bye','good bye','see ya']:
            if 'open' in query or 'take' in query:
                comm = query.strip().split(' ')
                task_list(comm[-1])
            elif 'write' in query:
                speak("sure")
                val = get_gpt(query)
                print(val+"\n")
            else:
                val = get_gpt(query)
                print("KODI:",val)
                speak(val)
                
        else:
            val = get_gpt(query)
            print("KODI:",val)
            speak(val)
            return -1
    except sr.UnknownValueError:
        query = 'None'
        return query
    
greetuser()
while True:
    code = take_user_input()
    if code == -1:
        break