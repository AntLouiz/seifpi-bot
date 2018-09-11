from telegram.ext import Updater
from handlers import (
    start_handler,
    help_handler,
    # get_movie_handler,
    default_handler,
)
from settings import TELEGRAM_BOT_TOKEN


def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(default_handler)
    # dispatcher.add_handler(get_movie_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
