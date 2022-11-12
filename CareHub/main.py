import logging
import tkinter_gui
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import CommandHandler

from threading import Thread

# Global Variables
# Todo: Make this safer!
APItoken = "5597776676:AAG9mMM2BhWv9y10CQ3ooDaVhokWo3cg9fo"

update_mood = 0

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
    global update_mood

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


def start_bot():
    application = ApplicationBuilder().token(APItoken).build()
    update_handler = CommandHandler('update', update_pls)
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(update_handler)
    application.run_polling()

if __name__ == '__main__':

    tkinter_window = tkinter_gui.TkinterWindow()
    start_bot()
