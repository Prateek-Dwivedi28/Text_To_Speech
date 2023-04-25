# RoboSpeaker For Mac

import os

if __name__ == '__main__':
    print("Welcome To RoboSpeaker 1.1. Created By Prateek")
    while True:
        x = input("Type quit to exit \n Enter What You Want Me To Speak: ")
        if x=='quit':
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"

    os.system(command)

#RoboSpeaker For Windows

import pyttsx3
if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    print("Welcome To RoboSpeaker 1.1. Created By Prateek")
    while True:
        word = input("Type quit to exit \n Enter What You Want Me To Speak: ")
        if word == 'quit':
            text_to_speech.say(word)
            text_to_speech.runAndWait()
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()
        
