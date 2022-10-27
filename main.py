import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import CommandHandler
from tkinter import *
import secrets

import webbrowser, os, sys
from os import listdir

# Global Variables
# Todo: Make this safer!
APItoken = "5597776676:AAG9mMM2BhWv9y10CQ3ooDaVhokWo3cg9fo"
update_mood = 0
pictures = 0



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message( chat_id=update.effective_chat.id, text=
        "/update To force an update on the users screen \n" +
        "/show_pictures To view all the pictures currently on the frame \n" +
        "or reply to this message with a picture to add it to the digital frame!")

async def show_pictures(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global pictures
    str_pictures = str(pictures)
    await context.bot.send_message( chat_id=update.effective_chat.id, text="There are currently " + str_pictures + " pictures on the frame!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=
    "/update To force an update on the users screen")


# Test function 1
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    numbers = context.args

    numberslist = numbers[0].split(",")

    # await context.bot.send_message(chat_id=update.effective_chat.id, text="please wait")
    result = calculator(numberslist[0], numberslist[1])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)


def calculator(nr1, nr2):
    return int(nr1) + int(nr2)


# test function 2
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stores the photo and asks for a location."""
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    print("got a pic!!!!")
    await photo_file.download("user_photo.jpg")
    await update.message.reply_text(
        "Photo received!"
    )
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    print("got the caps command")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


async def call(update: Update, context: ContextTypes.DEFAULT_TYPE):
    generated_URL = "https://meet.jit.si/" + secrets.token_urlsafe()
    url = generated_URL

    chrome_path = '/usr/lib/chromium-browser/chromium-browser'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=generated_URL)
    webbrowser.get(chrome_path).open(url)


async def update_pls(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global update_mood
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sending update request to CareHub! Please wait for a response.")

    update_mood = draw_window()
    if update_mood == 1:
        update_answer = "USER IS HAPPY! :)"
    elif update_mood == 2:
        update_answer = "USER IS SAD! :("
    else:
        update_answer = "Something went wrong..."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=update_answer)


def clicked_sad(window):
    global update_mood
    print("Sad Button was clicked")
    update_mood = 2
    window.destroy()


def clicked_happy(window):
    global update_mood
    print("Happy Button was clicked")
    update_mood = 1
    window.destroy()


def draw_window():
    global update_mood
    window = Tk()
    window.title("CareHub")
    window.attributes("-fullscreen", True)
    window.focus_set()
    btn_happy = Button(window, text="Am Happy :)!", bg="#5cfac3", height=50, width=75,
                       command=lambda: clicked_happy(window))
    btn_happy.pack(side='right')

    btn_sad = Button(window, text="Am Sad :(!", bg="#fa7070", height=50, width=75, command=lambda: clicked_sad(window))
    btn_sad.pack(side='left')

    window.mainloop()
    return update_mood


if __name__ == '__main__':


    application = ApplicationBuilder().token(APItoken).build()

    folder_dir = os.getcwd()
    for images in os.listdir(folder_dir):
        # check if the image ends with png
        if (images.endswith(".png") or images.endswith(".jpg")):
            print(images)
            pictures = pictures + 1



    start_handler = CommandHandler('start', start)
    show_handler = CommandHandler('show_pictures', show_pictures)
    caps_handler = CommandHandler('caps', caps)
    calc_handler = CommandHandler("calc", calc)
    update_handler = CommandHandler('update', update_pls)
    call_handler = CommandHandler('call', call)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    image_handler = MessageHandler(filters.PHOTO, photo)

    application.add_handler(start_handler)
    application.add_handler(image_handler)
    application.add_handler(show_handler)
    application.add_handler(calc_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(call_handler)

    application.add_handler(update_handler)

    # Handler must be last
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()
