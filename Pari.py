import pyttsx
import aiml
import os
import speech
engine=pyttsx.init()
k=aiml.Kernel()
k.loadBrain("Omegle.brn") # Knowledge Base of Prati
k.setBotPredicate("name","Pari") #Name
k.setBotPredicate("age","Well i'm 16 years old, how old are u?") #Prati's Age
k.setBotPredicate("gender","Female")
k.setBotPredicate("location","India") #Location of Prati
k.setBotPredicate("birthday","12th May, 1997") #Birthdate of Prati
k.setBotPredicate("nationality","Indian") #Nationality of Prati
# To change the voice of the bot, go to control panel -> select speech recognition -> Select text to speech and select a voice from there.
while True:
    phrase = speech.input() #Speech to text converter, phrase variable contains the converted text
    engine.say(k.respond(phrase)) #Text to speech converter
    engine.runAndWait()
    if phrase == "Ok, see ya Prati": #To stop talking to Prati, replace Prati with name of your choice.
        break
