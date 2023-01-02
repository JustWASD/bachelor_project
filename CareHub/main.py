#Telegram
from telegram import Update
import telegram
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

#Standard
import logging
import secrets


import cfg
import tkinter_gui
#import browser_and_calling

#Schedular
import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("message: ", update.message.chat_id, "effictive_chat: ", update.effective_chat.id)

    if cfg.user_id_list.count(update.effective_chat.id) > 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Hallo! Hier erhalten Sie Benachrichtigungen"
                                            "von CareHub.\n"
                                            "Schicken Sie /update in den Chat um CareHub nach"
                                            "einem Stimmungs-Update zu fragen!")
    else:
        print("Unknown user tried to use the bot!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="You are not an authorized user!")

def call_scheduled_update():
    asyncio.run(scheduled_update())

async def scheduled_update():
    await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[2], #group_chat ID
                                                 text="Ein zeitliches Update wurde an CareHub geschickt! "
                                                      "Bitte warten Sie bis die Antwort kommt.")
    cfg.update_mood = gui.draw_window_thread()

    # TODO: This while is blocking and waiting for a response.
    # A better solution could be implemented but it is working for now.
    while cfg.update_mood == 0:
        True
    if cfg.update_mood == 1:
        update_answer = "CareHub Rückmeldung: \"Mir geht es gut! :)\""
        cfg.update_mood = 0
    elif cfg.update_mood == 2:
        update_answer = "CareHub Rückmeldung: \"Mir geht es leider nicht gut! :(\""
        cfg.update_mood = 0
    else:
        update_answer = "Irgendetwas hat nicht funktioniert!"
        print("Update broke...?!")

    await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[2],  # group_chat ID
                                                 text=update_answer)


async def update_pls(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #print(update)
    #print(context)
    if cfg.user_id_list.count(update.effective_chat.id) > 0:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Ein Update wird an CareHub geschickt! Bitte warten Sie bis die Antowort kommt.")

        cfg.update_mood = gui.draw_window_thread()

        #TODO: This while is blocking and waiting for a response.
        # A better solution could be implemented but it is working for now.
        while cfg.update_mood == 0:
            True
        if cfg.update_mood == 1:
            update_answer = "CareHub Rückmeldung: \"Mir geht es gut! :)\""
            cfg.update_mood = 0
        elif cfg.update_mood == 2:
            update_answer = "CareHub Rückmeldung: \"Mir geht es leider nicht gut! :(\""
            cfg.update_mood = 0
        else:
            update_answer = "Irgendetwas hat nicht funktioniert!"
            print("Update broke...?!")

        await context.bot.send_message(chat_id=update.effective_chat.id, text=update_answer)
    else:
        print("Unknown user tried to use the bot!")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="You are not an authorized user!")


async def send_call_notification(user_index):

    generated_URL = "https://meet.jit.si/" + secrets.token_urlsafe()
    cfg.url = generated_URL

    await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[user_index],
                                                 text="Hallo! Ich möchte gerne Videotelefonieren!\n"
                                                      "Du findest mich unter folgendem Link:")
    if await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[user_index], text=cfg.url):
        print("Call notification sent!")
        return 1

async def send_call_failed_notification(user_index):

    await telegram.Bot(cfg.APItoken).sendMessage(chat_id=cfg.user_id_list[user_index],
                                                 text="Es ist leider zu lange Zeit vergangen und "
                                                      "der Videocall wurde beendet!\n"
                                                      "Meld dich bitte bei Gelegenheit!")
    print("Call Failed notification sent!")



if __name__ == '__main__':
    
    application = ApplicationBuilder().token(cfg.APItoken).build()
    update_handler = CommandHandler('update', update_pls)
    start_handler = CommandHandler('start', start)

    application.add_handler(start_handler)
    application.add_handler(update_handler)

    scheduler = BackgroundScheduler()

    update_trigger = OrTrigger([CronTrigger(hour=8, minute=30),
                                CronTrigger(hour=12, minute=0),
                                CronTrigger(hour=16, minute=30)])

    scheduler.add_job(call_scheduled_update, update_trigger)
    scheduler.start()

    gui = tkinter_gui.TkinterWindow()

    application.run_polling()
