from datetime import datetime
data = {'Name': [] , 'ages': []}
names = []
birtdates = []
def get_day(date):
    date_obj = datetime.strptime(date,'%d-%m-%Y')
    return date_obj.strftime("%A")

def get_inputes():
    flag = True
    while(flag):
        user_input = input("Name,date? ")
        if (len(user_input) > 0):
            x = user_input.index(',')
            names.append(user_input[:x])
            birtdates.append(user_input[x+2:])
        else:
            flag = False
    print_result()
def calculte_age(name,date):
    date_now = datetime.now()
    try:
        date_obj = datetime.strptime(date,'%d-%m-%Y')
        if(date_now.month >= date_obj.month):
            return date_now.year - date_obj.year
        else:
            return date_now.year - date_obj.year - 1
    except ValueError:
        return 'Invalid Date'
    
def print_result():
    for i in range(len(names)):
        calculte_age(birtdates[i])
        #print(names[i], ' is', calculte_age(birtdates[i]), ' years old and she/he was born on ', get_day(birtdates[i]))

def age_rearrange():
    
get_inputes()

