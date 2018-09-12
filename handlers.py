import time
import telegram
import tmdbsimple as tmdb
from telegram.ext import (
    Filters,
    CommandHandler,
    RegexHandler,
    MessageHandler
)
from emoji import emojize
from decouple import config
from utils import (
  get_schedules,
  get_date,
  get_time_delta,
  get_now_schedules
)


def start(bot, update):

    msg = "Olá, sou o Bot do SEIFPI."

    bot.send_message(
        chat_id=update.message.chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )

def support(bot, update):
  """
    Shows a help message.
  """

  msg = "Alguma mensagem de suporte."

  bot.send_message(
      chat_id=update.message.chat_id,
      text=msg,
      parse_mode=telegram.ParseMode.MARKDOWN
  )


def default(bot, update):
  """
    A default message to unknown command messages.
  """

  msg = "Desculpe, nao entendi sua mensagem."
  msg += emojize(':pensive:', use_aliases=True)

  bot.send_message(
      chat_id=update.message.chat_id,
      text=msg,
      parse_mode=telegram.ParseMode.MARKDOWN
  )

def now(bot, update):
  """
    A command message to show what is in working.
  """

  success_message = 'Atividades sendo desenvolvidas:\n'
  error_message = 'Nenhuma atividade no momento.'

  now_schedules = get_now_schedules()

  if len(now_schedules):
    bot.send_message(
      chat_id=update.message.chat_id,
      text=success_message
    )

    for schedule in now_schedules:
      bot.send_message(
        chat_id=update.message.chat_id,
        text="-{}".format(schedule['title']),
        parse_mode=telegram.ParseMode.MARKDOWN
      )
  else:
    bot.send_message(
      chat_id=update.message.chat_id,
      text=error_message
    )

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('support', support)
now_handler = CommandHandler('now', now)
default_handler = MessageHandler(Filters.command, default)
