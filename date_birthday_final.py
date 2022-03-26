from datetime import datetime
data = []
def get_day(date):
    date_obj = datetime.strptime(date,'%d-%m-%Y')
    return date_obj.strftime("%A")

def get_inputs():
    flag = True
    while (flag):
        user_input = input("name,date of birth? ")
        if (len(user_input) > 0):
            try:
                data.append({'Name': user_input[:user_input.index(',')], 'Age':cal_age(user_input[:user_input.index(',')],user_input[user_input.index(',')+2:]),'Day': get_day(user_input[user_input.index(',')+2:])})
            except ValueError:
                print("Invalid Data in : ", user_input[:user_input.index(',')])
        else:
            flag = False
    print_result()
def print_result():
    new_data = sorted(data, key=lambda data: data['Name'], reverse=True)
    for i in range(len(new_data)):
        print(new_data[i]['Name'], ' is ', new_data[i]['Age'], ' Years old she/he was born on ' , new_data[i]['Day'])
    if(len(new_data) > 1):   
        print("The Oldest one is ", new_data[0]['Name'])
        print("The Yougest one is ", new_data[-1]['Name'])
        print("Total People: ", len(new_data))
    else:
        print("There is no oldest or youngest person")
    

def cal_age(name,date):
    date_now = datetime.now()
    try:
        date_obj = datetime.strptime(date,'%d-%m-%Y')
        if(date_now.month >= date_obj.month):
            return date_now.year - date_obj.year
        else:
            return date_now.year - date_obj.year - 1
    except ValueError:
        print("Invalid Date in ", name)

            
get_inputs()
