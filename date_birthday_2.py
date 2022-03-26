from datetime import datetime
week_names = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
data = {'name': [], 'birtdates': [], 'ages': [], 'day': []}
date = datetime.now()
def get_userinputs():
    flag = True
    while(flag):
        user_input = input("Pelase input Name,date: ")
        if (len(user_input) > 0):
            data['name'].append(user_input[:user_input.index(',')])
            data['birtdates'].append(user_input[user_input.index(',')+2:])
        else:
            flag = False

    calculate_age()
def calculate_age():
    for birtdate in data['birtdates']:
        date_old = format_date(birtdate)
        if (date.month >= date_old.month):
            data['ages'].append(date.year-date_old.year)
        else:
            data['ages'].append(date.year-date_old.year-1)

def format_date(birtdate):
    date_obj = datetime.now()
    try:
        date_obj = datetime.strptime(birtdate,"%d-%m-%Y")
        day = get_day(date_obj)
    except ValueError as er:
        print("[DEBUG] ", er)
    return date_obj


def print_result():
    for name in data['name']:
        print(name, " is ", data['ages'][data['name'].index(name)], " years old and she/he was born on ", data['day'][data['name'].index(name)],'day')

def get_day(birtdate):
    th_day = birtdate.ctime()
    for day in week_names :
        if (th_day.find(day) > -1):
            data['day'].append(day)

get_userinputs()
print_result()
