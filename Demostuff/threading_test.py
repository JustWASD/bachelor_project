import logging
import secrets
import asyncio
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from telegram import Update
import telegram
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk


import threading

# Global Variables
# Todo: Make this safer!
APItoken = "5597776676:AAG9mMM2BhWv9y10CQ3ooDaVhokWo3cg9fo"

my_font = " "
update_mood = 0
pictures = 0
sent_msg = 0
url = " "
call_connect = " "

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

    global user_id, url

    generated_URL = "https://meet.jit.si/" + secrets.token_urlsafe()
    url = generated_URL


    await telegram.Bot(APItoken).sendMessage(chat_id=user_id[user], text="Hello, i'd like to video chat with you!")
    if await telegram.Bot(APItoken).sendMessage(chat_id=user_id[user], text=generated_URL):
        print("nachricht gesendet")
        return 1


    
def start_call():
    global call_connect
    connected = 0

    chrome_options = Options()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--kiosk");
    chrome_options.add_argument("use-fake-ui-for-media-stream")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(4)
    login = driver.find_element(By.CLASS_NAME, 'field  ')
    driver.find_element(By.CLASS_NAME, 'chrome-extension-banner__close-container').click()
    
    
    #logs in 
    login.send_keys("Gast")
    login.send_keys(Keys.RETURN)
    
    # wait 2min30secs for second person to join the call
    try:
        WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'stage-participant-label')))
        connected = 1
    except: 
        connected = 0
        print("timed out!")

    
    
    if connected == 1:
        call_connect.destroy()
        print("connected")
        while True:
            try:
                WebDriverWait(driver, 3).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'stage-participant-label')))
            except:  
                print("call ended")
                driver.close()
                connected = 0
                break
            time.sleep(5)
    else:
        print("no connection established")
        call_connect.config(bg="red")
        driver.close()
        time.sleep(20)
        call_connect.destroy()
    

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


        # The Label widget is a standard Tkinter widget used to display a text or happy_icon on the screen.
        picture = Button(self.root, image=img, command=self.draw_call)

        # The Pack geometry manager packs widgets in rows or columns.
        picture.pack(fill=BOTH)


        self.root.mainloop()

    def draw_window_thread(self):
        global update_mood
        
        update_window = Toplevel(self.root)
        update_window.title("CareHub")
        update_window.attributes("-fullscreen", True)
        update_window.focus_set()

        happy_icon = Image.open("happy_icon.png")
        happy_icon = happy_icon.resize((100, 100), Image.LANCZOS)
        # Convert the happy_icon to PhotoImage
        happy_img = ImageTk.PhotoImage(happy_icon)

        sad_icon = Image.open("sad_icon.png")
        sad_icon = sad_icon.resize((100, 100), Image.LANCZOS)
        # Convert the happy_icon to PhotoImage
        sad_img = ImageTk.PhotoImage(sad_icon)

        my_font = font.Font(size=40, weight="bold")

        
        btn_happy = Button(update_window,width=15, image=happy_img, text="I Am Happy!", compound= TOP, bg="#5cfac3", font=my_font, command=lambda: self.clicked_happy(update_window))
        btn_sad = Button(update_window, width=15, image=sad_img, text="I Am Sad!", bg="#fa7070", compound= TOP, font=my_font, command=lambda: self.clicked_sad(update_window))
        
         #Something about garbage collection... Doesnt work otherwise. Yey.
        btn_happy.image = happy_img
        btn_sad.image = sad_img
        
        
        btn_happy.pack(side=RIGHT, fill=BOTH, expand=1, padx=5, pady=5)
        btn_sad.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)

        return update_mood
    
    def draw_wait_window(self):
        global call_connect
        
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
        my_font = font.Font(size=14, weight="bold")


        screen_width = call_window.winfo_screenwidth()
        screen_height = call_window.winfo_screenheight()

        bild1.thumbnail((int(screen_width / 2), int(screen_height / 2)))
        bild2.thumbnail((int(screen_width / 2), int(screen_height / 2)))
        bild3.thumbnail((int(screen_width / 2), int(screen_height / 2)))

        bild1 = ImageTk.PhotoImage(bild1)
        bild2 = ImageTk.PhotoImage(bild2)
        bild3 = ImageTk.PhotoImage(bild3)

        btn1 = Button(call_window, width=int(screen_width / 4), image=bild1, text="Sabrina anrufen", compound=TOP,
                      font=my_font)
        btn2 = Button(call_window, width=int(screen_width / 4), image=bild2, text="Gabriel anrufen", compound=TOP,
                      font=my_font, command= lambda: call_gabs(call_window))
        btn3 = Button(call_window, width=int(screen_width / 4), image=bild3, text="Krankenschwester anrufen",
                      compound=TOP, font=my_font)
        btn4 = Button(call_window, width=int(screen_width / 4), bg="#fa7070", text="Close", command=call_window.destroy,
                      font=my_font)

        #Something about garbage collection... Doesnt work otherwise. Yey.
        btn1.image = bild1
        btn2.image = bild2
        btn3.image = bild3

        btn1.pack(side=LEFT, fill=BOTH, expand=1)
        btn2.pack(side=LEFT, fill=BOTH, expand=1)
        btn3.pack(side=LEFT, fill=BOTH, expand=1)
        btn4.pack(side=LEFT, fill=BOTH, expand=1)

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

    success = asyncio.run(call(0))
    
    if success == 1:
        browser_thread = threading.Thread(target=start_call)
        browser_thread.start()
        
        time.sleep(5)
        tkinter_window.draw_wait_window()
        call_window.destroy()
        
    








tkinter_window = TkinterWindow()
start_bot()
