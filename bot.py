import logging
import os
from covid19 import covid_india_data, covid_world_data
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "your token here obtained from bot father"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(token='paste your token here', use_context=True)
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! My Name is Dustie. How can I help You?\nCurrently i can only give you updates on '
                              'CoronaVirus\nUse /help to see what i can perform')


def covidindia(update, context):
    """Send a message when the command /covidinida is issued."""
    update.message.reply_text(''.join(covid_india_data()))


def covidworld(update, context):
    """Send a message when the command /covidinida is issued."""
    update.message.reply_text(''.join(covid_world_data()))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Use /covidindia to get updates on coronavirus situation on india\nUse /covidworld to '
                              'get updates on coronavirus situation of world')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text("Sorry InValid Command. \nPlease use /help to see what i can perform")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("covidindia", covidindia))
    dp.add_handler(CommandHandler("covidworld", covidworld))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook("https://app.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
