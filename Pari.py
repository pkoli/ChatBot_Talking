import pyttsx
import aiml
import os
import speech
engine=pyttsx.init()
k=aiml.Kernel()
k.loadBrain("Omegle.brn") # Knowledge Base of Pari
k.setBotPredicate("name","Pari") #Name
k.setBotPredicate("age","Well i'm 21 years old, how old are u?") #Pari's Age
k.setBotPredicate("gender","Female")
k.setBotPredicate("location","India") #Location of Pari
k.setBotPredicate("birthday","12th May, 1997") #Birthdate of Pari
k.setBotPredicate("nationality","Indian") #Nationality of Pari
# To change the voice of the bot, go to control panel -> select speech recognition -> Select text to speech and select a voice from there.
while True:
    phrase = speech.input() #Speech to text converter, phrase variable contains the converted text
    engine.say(k.respond(phrase)) #Text to speech converter
    engine.runAndWait()
    if phrase == "Ok, see ya Pari": #To stop talking to Pari, replace Pari with name of your choice.
        break
