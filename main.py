import os
from dotenv import load_dotenv
from pytimeparse import parse
import ptbot

load_dotenv()

TG_TOKEN = os.environ['TG_TOKEN']
TG_CHAT_ID = os.environ['TG_CHAT_ID']

def reply(chat_id, text):
    message_id = bot.send_message(chat_id, "Запускаю таймер...")
    seconds = parse(text)
    bot.create_countdown(seconds, notify_progress, chat_id=chat_id, message_id=message_id, total=seconds)
    bot.create_timer(seconds, notify, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id, total):
    progress_bar = render_progressbar(total, total - secs_left)
    bot.update_message(chat_id, message_id, "Осталось {} секунд\n{}".format(secs_left, progress_bar))

def notify(chat_id):
    bot.send_message(chat_id, "Время вышло")

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)

def main():
    global bot
    bot = ptbot.Bot(TG_TOKEN)
    bot.send_message(TG_CHAT_ID, "Бот запущен")
    bot.reply_on_message(reply)
    bot.run_bot()

if __name__ == "__main__":
    main()