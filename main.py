from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi',
    'hii',
    'hi there!',
    'what is your name ?',
    'My name is bot, I am created by Ayush ',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'Where do you live?',
    'I live in mumbai',
    'In which language do you talk? ',
    'I mostly talk in english'
]

trainer = ListTrainer(bot)
# training the bot
trainer.train(convo)

# answer = bot.get_response("what is your name ?")
# print(answer)

# print("Talk to bot")
# while True:
#     query = input()
#     if query == 'bye':
#         break
#     answer = bot.get_response(query)
#     print(answer)

main = Tk()

main.geometry("500x650")
main.title("My ChatBot")

img = PhotoImage(file="bot2.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)

def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("try speaking, your bot is listening ")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_bot()
        except Exception as e:
            print(e)
            print("Not recognized")

def ask_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You: " + query)
    msgs.insert(END, "bot: " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)

msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="ASK BOT", font=('Verdana', 20), command=ask_bot)
btn.pack()


# creating a function

def enter_function(event):
    btn.invoke()


main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)
t.start()

main.mainloop()
