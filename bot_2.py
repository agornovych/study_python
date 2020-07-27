import requests
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from datetime import date, timedelta

TG_TOKEN = '1171292940:AAHYSJbTS_DZGgI3_SOANX3_ks8PkB8liFg'
BASE_URL = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?'


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'anonim'

    text = update.effective_message.text
    if  text == '/start':
        reply_text = f"Hi, {name}!\n\n/USD for US dollar\n\n/EUR for Euro\n\n/ALL for all (don't use this button)\n\n /USD_7 weekly data\n\n /EUR_7 weekly data"
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )
    elif  text == '/USD':
        cc = 'usd'
        data = exchange(cc)
        reply_text = f'{data[0]} ({data[1]}): {data[2]} uah'
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )
    elif text == '/USD_7':
        cc = 'usd'
        data = cur_7(cc)
        reply_text = ''
        for f in range(1, 7 + 1):
            temp = f"{data[-f]['exchangedate']} >>> {data[-f]['cc']} >>> {data[-f]['rate']}\n"
            reply_text+=temp
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
        )
    elif text == '/EUR_7':
        cc = 'eur'
        data = cur_7(cc)
        reply_text = ''
        for f in range(1, 7 + 1):
            temp = f"{data[-f]['exchangedate']} >>> {data[-f]['cc']} >>> {data[-f]['rate']}\n"
            reply_text+=temp
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
        )
    elif  text == '/EUR':
        cc = 'eur'
        data = exchange(cc)
        reply_text = f'{data[0]} ({data[1]}): {data[2]} uah'
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )
    elif  text == '/ALL':
        reply_text = cur_all_data()
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )
    elif in_range(text) != True:
        reply_text = f"{name}, все херня, давай по новой!"
        bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )
    else:
        data = exchange(text)
        reply_text = f"{data[0]} ({data[1]}): {data[2]} auh"
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


def exchange(cc):
    url = str(f'{BASE_URL}valcode={cc}&json')
    resp = requests.get(url).json()[0]
    return resp['cc'], resp['txt'], resp['rate']


def cur_all():
    response = requests.get(f'{BASE_URL}json').json()
    result =[]
    for i in range(len(response)):
        result.append(response[i]['cc'].lower())
    return result


def cur_all_data():
    response = requests.get(f'{BASE_URL}json').json()
    result =''
    for i in range(len(response)):
        result+= f"{response[i]['cc']} >>> {response[i]['txt']} >>> {response[i]['rate']}\n"
    return result


def in_range(cc):
    expected = cur_all()
    if cc.lower() in expected:
        return True


def cur_7(cc, days = 7):
    today = date.today()
    minus_day = timedelta(days=-1)
    result = []
    result.append(str(today).replace('-', ''))
    for i in range(days-1):
        today +=minus_day
        result.append(str(today).replace('-', ''))
    fin=[]
    for j in result:
        url = str(f'{BASE_URL}valcode={cc}&date={j}&json')
        resp = requests.get(url).json()[0]
        fin.append(resp)
    return fin


if __name__ == '__main__':
    main()