import os
import subprocess as sp
import pywhatkit as kit

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'chrome': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'vscode': "C:\\Users\\BITS-N-BYTES\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe",
    'msedge' : "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
}

def open_chrome():
    os.startfile(paths['chrome'])

def play_on_youtube(video):
    kit.playonyt(video)

def open_calculator():
    sp.Popen(paths['calculator'])

def open_vscode():
    os.startfile(paths['vscode'])

def open_edge():
    os.startfile(paths['msedge'])

def open_cmd():
    p = sp.Popen(["start", "cmd", "/k", "{command here}"], shell = True)
    p.wait() 

