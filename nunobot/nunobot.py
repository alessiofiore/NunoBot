import logging
 
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
 
bot = Bot(token='269215629:AAFhzims_uzD1nJJQJB3cq6Wq4vM1W0tol4')
print(bot.get_me())
 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
 

def start(bot, update):
    print("start")
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    print("echo")
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    
def unknown(bot, update):
    print("unknown")
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

updater = Updater(token='269215629:AAFhzims_uzD1nJJQJB3cq6Wq4vM1W0tol4')

dispatcher = updater.dispatcher
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = CommandHandler('echo', echo)
dispatcher.add_handler(echo_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
 
updater.start_polling()
updater.idle()