from datetime import datetime
name_age = {'names': [], 'age': []}
user_inputs = []
input_r = ''
now = datetime.now()
weak_names = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
flag = True
day = ''
def format_inpute(user_input):
    div = user_input.index(',')
    name = user_input[:div]
    date = user_input[div+2:]
    age = calculate_age(date)
    name
    print_result(name,age)

def calculate_age(date):
    date_obj = ''
    
    try:
        date_obj = datetime.strptime(date,"%d-%m-%Y")
    except ValueError:
        print("invalid date")
    for days in weak_names:
        if (c.find(days) != -1):
            day = days
    return now.year - date_obj.year
def print_result(name,age):
    print(name, " is", age , "years old and she/he was born on ",day)

while(flag):
    input_r = input("input name,birthdate: ")
    if (len(input_r) > 0):
        user_inputs.append(input_r)
    else:
        flag = False
    
for user_input in user_input:
    format_inpute(user_input)
