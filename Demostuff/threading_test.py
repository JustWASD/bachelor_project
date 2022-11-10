import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import CommandHandler
from tkinter import *
from PIL import Image, ImageTk

import threading

# Global Variables
# Todo: Make this safer!
APItoken = "5597776676:AAG9mMM2BhWv9y10CQ3ooDaVhokWo3cg9fo"
update_mood = 0
pictures = 0

user_id = [927737771, 177508822]

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("message: ", update.message.chat_id, "effictive_chat: ", update.effective_chat.id)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=
    "/update To force an update on the users screen \n" +
    "/show_pictures To view all the pictures currently on the frame \n" +
    "or reply to this message with a picture to add it to the digital frame!")


async def update_pls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global update_mood, user1_id, user2_id
    # chat_id=update.effective_chat.id,
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sending update request to CareHub! Please wait for a response.")

    update_mood = tkinter_window.draw_window_thread()

    while(update_mood == 0):
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



def tinkterpic():
    window = Tk()
    window.title("CareHub")
    window.attributes("-fullscreen", True)

    path = "tattooidee.jpg"

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img = ImageTk.PhotoImage(Image.open(path))

    #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    panel = Label(window, image = img)

    #The Pack geometry manager packs widgets in rows or columns.
    panel.pack(fill="none")

    #Start the GUI
    window.mainloop()




class Tkinter_Window(threading.Thread):

    #starts the thread
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        #solves the error TCL_AsyncDelete
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("CareHub")
        self.root.attributes("-fullscreen", True)

        path = "tattooidee.jpg"

        img = ImageTk.PhotoImage(Image.open(path))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = Label(self.root, image=img)

        # The Pack geometry manager packs widgets in rows or columns.
        panel.pack(fill="none")
        self.root.mainloop()

    def draw_window_thread(self):
        global update_mood
        update_window = Toplevel(self.root)
        update_window.title("CareHub")
        update_window.attributes("-fullscreen", True)
        update_window.focus_set()
        btn_happy = Button(update_window, text="Am Happy :)!", bg="#5cfac3", height=50, width=75,
                           command=lambda: tkinter_window.clicked_happy(update_window))
        btn_happy.pack(side='right')

        btn_sad = Button(update_window, text="Am Sad :(!", bg="#fa7070", height=50, width=75,
                         command=lambda: tkinter_window.clicked_sad(update_window))
        btn_sad.pack(side='left')

        return update_mood

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



tkinter_window = Tkinter_Window()


def telegram_bot():
    application = ApplicationBuilder().token(APItoken).build()
    update_handler = CommandHandler('update', update_pls)
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(update_handler)
    application.run_polling()


bot_thread = threading.Thread(target=telegram_bot(), daemon=True)

bot_thread.start()


