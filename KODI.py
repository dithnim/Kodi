import speech_recognition as sr
from random import choice
import random
from functions import os_ops
import os
import elevenlabs
import openai
import pyscreenshot as ImageGrab
import string


USERNAME = "Adam"
BOTNAME = "Kodi"

chat_gpt_api = "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"
openai.api_key = chat_gpt_api

def task_list(command):
    if command in ["calc","calculator","open calc","open calculator"]:
        speak("Opening the system calculator")
        os_ops.open_calculator()

    elif command in ["chrome","open google chrome","open google","google"]:
        speak("opening. google")
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
        speak("Screenshot saved")
        img.show()

    elif command == 'shutdown':
        speak("are you sure.")
        if (take_user_input() == 'yes'):
            speak("attempting system shutdown in. 3,  2,  1.")
            os.system("shutdown /s")
        else:
            speak("aborting system shutdown")



def get_gpt(prompt):
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'user','content':prompt}
        ]
    )
        return response['choices'][0]['message']['content']


def speak(text):
    audio = elevenlabs.generate(
        text= text,
        voice = 'Dave',
        api_key='95bed6567088b2c3f63ecd24376e2b80'
    )
    elevenlabs.play(audio)

def greetuser():
    speak(get_gpt(f"Your name is {BOTNAME} and your purpose is to be {USERNAME}'s AI assistant and tell the user to say 'hello' to activate"))

def take_user_input():
    global r;global audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...\n')
        query = r.recognize_google(audio)
        print("You said:",query)
        query = query.lower()
        if not 'exit' in query or 'stop' in query:
            if not 'open' in query or 'take' in query or 'write' in query:
                val = get_gpt(query)
                print("KODI:",val)
                speak(val)
            elif 'write' in query:
                speak("sure")
                val = get_gpt(query)
                print(val)
            else:
                comm = query.strip().split(' ')
                task_list(comm[-1])
        else:
            speak("Goodbye sir.")
            return query
    except sr.UnknownValueError:
        sorry_list = ['Sorry, I could not understand. Could you please say that again?',
                      'Can you repeat the question please?',
                      'I am sorry, Can you try again?',
                      'Sorry, I did not understand. Try checking if your microphone is working properly.',
                      'sorry, I did not hear anything. Try checking your microphone.']
        speak(sorry_list[0])
        query = 'None'
    return query

def listner():
    global r;global audio;global query
    try:
        print("Say 'Hello' to activate..!")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)

        print("Recognizing....\n")
        query = r.recognize_google(audio)
        print("You said:",query)
        query = query.lower()
        if query == 'hello':
            val = get_gpt("greet the user and ask for how to help")
            print("KODI:",val)
            speak(val)
            take_user_input()
    except sr.UnknownValueError:
        sorry_list = ['Sorry, I could not understand. Could you please say that again?',
                      'Can you repeat the question please?',
                      'I am sorry, Can you try again?',
                      'Sorry, I did not understand. Try checking if your microphone is working properly.',
                      'sorry, I did not hear anything. Try checking your microphone.']
        speak(sorry_list[0])
        
greetuser()
while True:
    take_user_input()