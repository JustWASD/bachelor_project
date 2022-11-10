import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import CommandHandler



# Global Variables
# Todo: Make this safer!
APItoken = "5597776676:AAG9mMM2BhWv9y10CQ3ooDaVhokWo3cg9fo"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)




if __name__ == '__main__':

    application = ApplicationBuilder().token(APItoken).build()

    application.run_polling()