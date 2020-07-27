import requests
from datetime import date, datetime, timedelta
import time
# HEADERS = {'user-agents': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'accept': '*/*'}

# url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
# valcode = str(input('Currency you need: '))
# url = str(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&json')


# def cur(cc):
#     response = requests.get(url)
#     resp_data = response.json()
#     n = len(resp_data)
#     temp = []
#     result = 'none'
#     for i in range(0, n):
#         temp = resp_data[i]
#         cc_val = temp.get('cc')
#         if cc_val.lower() == cc.lower():
#             result = temp.get('txt')
#             break
#     return result
BASE_URL = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?'

def timer(func):
    def wrapper(*args):
        start = time.time()
        print('start time', start)
        target = func(*args)
        end = time.time()
        print('end time', end)
        print('timer.Function execution time in seconds:', round(end - start, 6))
        print('timer.Function executed')
        print(func(*args))

    return wrapper


@timer
def exchange(cur):
    url = str(f'{BASE_URL}valcode={cur}&json')
    resp = requests.get(url).json()[0]
    return resp['cc'], resp['txt'], resp['rate'],resp['exchangedate']

def exchange(cur):
    url = str(f'{BASE_URL}valcode={cur}&json')
    resp = requests.get(url).json()[0]
    result = resp['cc'], resp['txt'], resp['rate']
    return result

print(exchange('usd'))


# yyyymmdd, де yyyy - рік, mm - місяць, dd - день

# def cur_7(c):
#     today = date.today()
#     minus_day = timedelta(days=+1)
#     result = []
#     result.append(str(today).replace('-', ''))
#     for i in range(7):
#         today = today-minus_day
#         result.append(str(today).replace('-', ''))


# def cur_7(cc, days = 7):
#     today = date.today()
#     minus_day = timedelta(days=-1)
#     result = []
#     result.append(str(today).replace('-', ''))
#     for i in range(days-1):
#         today +=minus_day
#         result.append(str(today).replace('-', ''))
#     fin=[]
#     for j in result:
#         url = str(f'{BASE_URL}valcode={cc}&date={j}&json')
#         resp = requests.get(url).json()[0]
#         fin.append(resp)
#         print(fin)
#     return fin
#     for f in range(1, days+1):
#         print(f"{fin[-f]['exchangedate']} ** {fin[-f]['cc']} ({fin[-f]['txt']}) ** {fin[-f]['rate']}")

#
# def cur_all_data():
#     response = requests.get(f'{BASE_URL}json').json()
#     result =''
#     for i in range(len(response)):
#         result+= f"{response[i]['cc']} >>> {response[i]['txt']} >>> {response[i]['rate']}\n"
#     return result
#
#
# print(cur_all_data())

#
# print(today)
# date=20200522
# def exchange(cur):
#     url = str(f'{BASE_URL}valcode={cur}&date={date}&json')
#     resp = requests.get(url).json()[0]
#     return resp['cc'], resp['txt'], resp['rate'],resp['exchangedate']
#
# print(exchange('usd'))

# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20200302&json

# print(url)
# rate = (dict(response.json()[0]))
# print(rate.get('rate', 'No value found'))



# if response:
#     print('Success!')
# else:
#     print('Not Found.')
#
# # status code
# print(response.status_code)
#
# # content
# print(response.content)
#
# # text
# print(response.text)
#
# # json
# print(response.json())
#
# # headers
# print(response.headers)
# print(response.headers['Content-Type'])
#
# # Content-Type
# print(response.headers['Content-Type'])
#
# https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json
#
# rate = (dict(response.json()[0]))
# print(rate)
# print(rate.get('rate', 'No value found'))
# print(rate.get('cc', 'No value found'))
# print(rate.get('exchangedate'))