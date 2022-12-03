#Telegram
from telegram import Update
import telegram
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

#Standard
import logging
import secrets
import asyncio
import time
import threading

import cfg
import tkinter_gui
import browser_and_calling


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


    # chat_id=update.effective_chat.id,
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Sending update request to CareHub! Please wait for a response.")

    cfg.update_mood = gui.draw_window_thread()

    #TODO: This while is needs to be changed.
    while cfg.update_mood == 0:
        True
    if cfg.update_mood == 1:
        update_answer = "USER IS HAPPY! :)"
        cfg.update_mood = 0
    elif cfg.update_mood == 2:
        update_answer = "USER IS SAD! :("
        cfg.update_mood = 0
    else:
        update_answer = "Something went wrong..."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=update_answer)


def call_user(user_index):
    
    
    success = asyncio.run(send_call_notification(user_index))

    if success == 1:
        browser_thread = threading.Thread(target=browser_and_calling.start_call)
        browser_thread.start()
        time.sleep(5)
        gui.draw_wait_window()
        cfg.choose_user_to_call_windows.destroy()
    

#TODO: Structure of this call must be changed and optimized.
async def send_call_notification(user_index):

    generated_URL = "https://meet.jit.si/" + secrets.token_urlsafe()
    cfg.url = generated_URL

    await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[user_index], text="Hello, i'd like to video chat with you!")
    if await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[user_index], text=cfg.url):
        print("nachricht gesendet")
        return 1



if __name__ == '__main__':
    
    application = ApplicationBuilder().token(cfg.APItoken).build()
    update_handler = CommandHandler('update', update_pls)
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(update_handler)

    gui = tkinter_gui.TkinterWindow()

    application.run_polling()
