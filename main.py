from turtle import update
from click import File
from telegram import Update , ParseMode 
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext , CommandHandler, ConversationHandler

import config
from plugin import encodebase64

FILE_NAME = range(1)

# Handlers
def send_file(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    print(update.message.text)
    update.message.reply_document(open(config.RUTA_DOWN,"rb"))

       
#CallBack
def recibirnameCallback(update, callback):
    update.message.reply_text("Envie el nombre del archivo")
    return FILE_NAME

def file_nameCallback(update, callback):
    """"Codificamo el archivo"""
    encodebase64.encodeb6(update.message.text)
    return ConversationHandler.END

def fallbackCallback(update,callback):
    update.message.reply_text("nombre no encontrado")


def main() -> None:
    """Start the bot."""
    # Creamos Updater y le pasamos el token
    updater = Updater(config.TOKEN)

    # Obtenemos el dispatcher para registrar los handlers
    dispatcher = updater.dispatcher

    # Handler para eco
    dispatcher.add_handler(CommandHandler("send", send_file))

    entry_points = [
        CommandHandler("enc",recibirnameCallback)
    ]

    states = {
        FILE_NAME: [
            MessageHandler(filters= Filters.text, callback= file_nameCallback)
        ]

    }

    fallback = [
        MessageHandler(filters = Filters.all, callback= fallbackCallback)
    ]

    dispatcher.add_handler(ConversationHandler(entry_points,states,fallback))


    # Iniciar el bot
    updater.start_polling()

    #Mantener el proceso hasta que se pulse Ctrl + C
    updater.idle()


if __name__ == '__main__':
    main()