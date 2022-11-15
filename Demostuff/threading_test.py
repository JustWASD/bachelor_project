import logging
import secrets
import asyncio
import time
import keyboard

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from telegram import Update
import telegram
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from tkinter import *
from PIL import Image, ImageTk
import webbrowser, os, sys
from os import listdir

import threading

# Global Variables
# Todo: Make this safer!
APItoken = "5597776676:AAG9mMM2BhWv9y10CQ3ooDaVhokWo3cg9fo"


update_mood = 0
pictures = 0
sent_msg = 0

user_id = [927737771, 177508822]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("message: ", update.message.chat_id, "effictive_chat: ", update.effective_chat.id)

    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="/update To force an update on the users screen \n" +
                                        "/show_pictures To view all the pictures currently on the frame \n" +
                                        "or reply to this message with a picture to add it to the digital frame!")


async def update_pls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global update_mood, user1_id, user2_id

    # chat_id=update.effective_chat.id,
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sending update request to CareHub! Please wait for a response.")

    update_mood = tkinter_window.draw_window_thread()

    while update_mood == 0:
        True
    if update_mood == 1:
        update_answer = "USER IS HAPPY! :)"
        update_mood = 0
    elif update_mood == 2:
        update_answer = "USER IS SAD! :("
        update_mood = 0
    else:
        update_answer = "Something went wrong..."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=update_answer)

async def call(user):

    global user_id

    generated_URL = "https://meet.jit.si/" + secrets.token_urlsafe()
    url = generated_URL
    
    chrome_options = Options()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--kiosk");
    chrome_options.add_argument("use-fake-ui-for-media-stream")
    #chrome_options.add_experimental_option("detach", True)

    # linux only
    #chrome_path = '/usr/lib/chromium-browser/chromium-browser'

    await telegram.Bot(APItoken).sendMessage(chat_id=user_id[user], text="Hello, i'd like to video chat with you!")
    await telegram.Bot(APItoken).sendMessage(chat_id=user_id[user], text=generated_URL)

    
    
    
    
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    time.sleep(3)
    login = driver.find_element(By.CLASS_NAME, 'field  ')

    login.send_keys("pycon")
    login.send_keys(Keys.RETURN)


    time.sleep(30)


    driver.close()
    

def start_bot():

    application = ApplicationBuilder().token(APItoken).build()
    update_handler = CommandHandler('update', update_pls)
    start_handler = CommandHandler('start', start)


    application.add_handler(start_handler)
    application.add_handler(update_handler)
    application.run_polling()




class TkinterWindow(threading.Thread):

    # starts the thread
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        # solves the error TCL_AsyncDelete
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("CareHub")
        self.root.attributes("-fullscreen", True)


        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        img = Image.open("Nasi.jpg")
        img.thumbnail((screen_width, screen_height))

        img = ImageTk.PhotoImage(img)


        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        picture = Button(self.root, image=img, command=self.draw_call)

        # The Pack geometry manager packs widgets in rows or columns.
        picture.pack(fill="none")
        # TODO: NOT WORKING
        # picture.bind("<Button-1>", draw_call())

        self.root.mainloop()

    def draw_window_thread(self):
        global update_mood
        update_window = Toplevel(self.root)
        update_window.title("CareHub")
        update_window.attributes("-fullscreen", True)
        update_window.focus_set()
        btn_happy = Button(update_window, text="Am Happy :)!", bg="#5cfac3", height=50, width=75,
                           command=lambda: self.clicked_happy(update_window))
        btn_happy.pack(side='right')

        btn_sad = Button(update_window, text="Am Sad :(!", bg="#fa7070", height=50, width=75,
                         command=lambda: self.clicked_sad(update_window))
        btn_sad.pack(side='left')

        return update_mood
    
    def draw_wait_window(self):
        
        call_connect = Toplevel(self.root)
        call_connect.title("Anruf")
        call_connect.attributes("-fullscreen", True)
        call_connect.focus_set()
        call_connect.config(bg="green")
        label1 = Label(call_connect, text="Bitte warten")
        label1.pack()
        
        #time.sleep(30)
        #call_connect.destroy()

    def draw_call(self):

        bild1 = Image.open("Sabi.jpg")
        bild2 = Image.open("Gabs.jpg")
        bild3 = Image.open("Dawg.jpg")

        call_window = Toplevel(self.root)
        call_window.title("Video Telefonat")
        call_window.attributes("-fullscreen", True)
        call_window.config(bg="black")
        call_window.focus_set()



        screen_width = call_window.winfo_screenwidth()
        screen_height = call_window.winfo_screenheight()

        bild1.thumbnail((int(screen_width / 2), int(screen_height / 2)))
        bild2.thumbnail((int(screen_width / 2), int(screen_height / 2)))
        bild3.thumbnail((int(screen_width / 2), int(screen_height / 2)))

        bild1 = ImageTk.PhotoImage(bild1)
        bild2 = ImageTk.PhotoImage(bild2)
        bild3 = ImageTk.PhotoImage(bild3)

        btn1 = Button(call_window, image=bild1)
        btn2 = Button(call_window, image=bild2, command=lambda: call_gabs(call_window))
        btn3 = Button(call_window, image=bild3)
        btn4 = Button(call_window, text="Close", command=call_window.destroy)

        #Something about garbage collection... Doesnt work otherwise. Yey.
        btn1.image = bild1
        btn2.image = bild2
        btn3.image = bild3




        btn1.grid(row=3, column=1)
        btn2.grid(row=3, column=3)
        btn3.grid(row=3, column=5)
        btn4.grid(row=3, column=7)


    def clicked_sad(self, update_window):
        global update_mood
        print("Sad Button was clicked")
        update_mood = 2
        update_window.destroy()

    def clicked_happy(self, update_window):
        global update_mood
        print("Happy Button was clicked")
        update_mood = 1
        update_window.destroy()

def call_gabs(call_window):
    call_window.destroy()
    time.sleep(3)
    tkinter_window.draw_wait_window()
    
    asyncio.run(call(0))









tkinter_window = TkinterWindow()
start_bot()
