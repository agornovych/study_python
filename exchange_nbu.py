import requests
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = '1171292940:AAHYSJbTS_DZGgI3_SOANX3_ks8PkB8liFg'
BASE_URL = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'аноним'

    text = update.effective_message.text
    a = list(exchange(text))
    reply_text = f"Привет, {name}!\n\nКурс {a[0]} на сегодня ({a[2]}): {a[1]}"
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )


def main():
    print('Start')
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=bot,
    )

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()
    print('Finish')


def exchange(cur):
    url = str(f'{BASE_URL}{cur}&json')
    response = requests.get(url)
    data = (dict(response.json()[0]))
    val = data.get('rate', 'No value found')
    cc = data.get('cc', 'No value found')
    exchangedate = data.get('exchangedate', 'No value found')
    return val, cc, exchangedate


if __name__ == '__main__':
    main()