# def formater(func):
#     def wrapper():
# # Виклик функції
#         request = func()
# # Підготовлений текст
#         template = '\nCEO Red Bull Inc.\nMr. John Bigbull\n\nHi John,\nI need the paid {0} from {3} to {4}.\n{1} {2}\n'
# # Форматування темплейту за допомогою словника, що передаються у виклику функції
#         print('@'*50 + template.format(request['vacation_type'], request['user_name'], request['user_surname'], request['date_from'], request['date_to']) + '@' * 50)
#     return wrapper()
#
# @formater
# def userdata():
#     vactype = int(input('Select you vacation type:\n1 for Vacation\n2 for Sick leave\n3 for Day off'))
# # Перевірка вводу на діапазон від 1 до 3
#     while vactype not in range(1, 4):
#         vactype = int(input('!!!!!!!!!!!Incorrect value!!!!!!!!!!!!\nTry again:\n1 for Vacation\n2 for Sick leave\n3 for Day off'))
# # Трансформація цифри в тип відпустки
#     if vactype == 1:
#         vactype = str('vacation')
#     elif vactype == 2:
#         vactype = str('sick leave')
#     else:
#         vactype = str('day off')
#     uname = input('Type your First name')
#     surname = input('Type your Surname')
# # Збір дат на вказану відпуству, де назва відпустки передається перемінною vactype
#     datefrom = input('Type start date of your ' + vactype + ' in format DD-Mmm')
#     dateto = input('Type end date of your ' + vactype + ' in format DD-Mmm')
# # Повертаю зібрані дані у вигляді словника
#     return {'vacation_type': vactype, 'user_name': uname, 'user_surname': surname, 'date_from': datefrom, 'date_to': dateto}



def print_twice(func):
    def wrapper():
        fileName = open("C:\\Users\\OGornovych\\Downloads\\log_test.txt", 'a')
        request = func()
        template = '\nCEO Red Bull Inc.\nMr. John Bigbull\n\nHi John,\nI need the paid {0} from {3} to {4}.\n{1} {2}\n'
        result = '@'*50 + template.format(request['vacation_type'], request['user_name'], request['user_surname'], request['date_from'], request['date_to']) + '@' * 50
        print(result)
        print('result:\n',  result, sep=' >>> ', end='/n', file=fileName)
    return wrapper()


@print_twice
def userdata():
    vactype = int(input('Select you vacation type:\n1 for Vacation\n2 for Sick leave\n3 for Day off'))
    while vactype not in range(1, 4):
        vactype = int(input('!!!!!!!!!!!Incorrect value!!!!!!!!!!!!\nTry again:\n1 for Vacation\n2 for Sick leave\n3 for Day off'))
    if vactype == 1:
        vactype = str('vacation')
    elif vactype == 2:
        vactype = str('sick leave')
    else:
        vactype = str('day off')
    uname = input('Type your First name')
    surname = input('Type your Surname')
    datefrom = input('Type start date of your ' + vactype + ' in format DD-Mmm')
    dateto = input('Type end date of your ' + vactype + ' in format DD-Mmm')
    return {'vacation_type': vactype, 'user_name': uname, 'user_surname': surname, 'date_from': datefrom, 'date_to': dateto}