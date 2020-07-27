def formater(func):
    def wrapper():
        r = func()
        print(f'\nCEO Red Bull Inc.\nMr. John Bigbull\n\nHi John,\nI need the paid {r[0]} from {r[3]} to {r[4]}.\n{r[1]} {r[2]}\n')

    return wrapper()


@formater
def userdata():
    req = []
    vactype = int(input('Select you vacation type:\n1 for Vacation\n2 for Sick leave\n3 for Day off'))
    while vactype not in range(1, 4):
        vactype = int(input(
            '!!!!!!!!!!!Incorrect value!!!!!!!!!!!!\nTry again:\n1 for Vacation\n2 for Sick leave\n3 for Day off'))
    if vactype == 1:
        req.append('vacation')
    elif vactype == 2:
        req.append('sick leave')
    else:
        req.append('day off')
    req.append(input('Type your First name'))
    req.append(input('Type your Surname'))
    req.append(input(f'Type start date of your {req[0]} in format DD-Mmm'))
    req.append(input(f'Type end date of your {req[0]} in format DD-Mmm'))
    return req

