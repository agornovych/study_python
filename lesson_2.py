# a new list to collect user data
userdata = dict()
# var VT to get vacation type
vt = int(input('''Choose your vacation request types by typing a number:
1 for Vacation
2 for Sick leave
3 for Day off'''))

# add vacation type to list USERDATA
vt1=vt
userdata['Vacation type'] = vt

# vacation type dict (can be moved to decorator lvl)
vacTypeList = {1: 'Vacation', 2: 'Sick leave', 3: 'Day off'}

# get user inputs to list USERDATA
userdata['First name'] = input('Type your First name')
userdata['Surname'] = input('Type your Surname')
userdata['From date'] = input('Type start date of your ' + vacTypeList[vt])
userdata['To date'] = input('Type end date of your ' + vacTypeList[vt])

# print to check what was added to var VT and list USERDATA
print('Results ' + '=' * 25)
print('1. Vacation type: ' + vacTypeList[vt])
print(userdata)
print('=' * 33)

# function to get user data
def getuserdata():
    return userdata
print(userdata)
