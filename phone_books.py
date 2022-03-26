flag = True
phone_numbers = {'names': ['Mohammed','Amal','Khadijah'], 'numbers':['1111111111','2222222222','3333333333']}


def print_all_number():
    for name in phone_numbers['names']:
        print("Name: ", name, "Number", phone_numbers['numbers'][phone_numbers['names'].index(name)])
def find_by_number(number):
    if (number in phone_numbers['numbers']):
        x = phone_numbers['numbers'].index(number)
        print("Name: ", phone_numbers['names'][x], "Number: ", phone_numbers['numbers'][x])
    else:
        print("sorry, the number not in the Phonebook")
def find_by_name(name):
    if (name in phone_numbers['names']):
        x = phone_numbers['names'].index(name)
        print("Name: ", phone_numbers['names'][x], "Number: ", phone_numbers['numbers'][x])
    else:
        print("sorry, the number not in the Phonebook")
def inser_number(name,number):
    phone_numbers['names'].append(name)
    phone_numbers['numbers'].append(number)
    print("Data Has been Add")

while (flag):
    print("------------Phone Book --------------")
    print("1 - Search By Number")
    print("2 - Search By Name")
    print("3 - insert new number and name")
    print("4 - Print All The Phonebook")
    print("5 - quit")
    choice = input("Choose: ")
    if (int(choice) == 1 ):
        number = input("What the number you want to search? ")
        if (len(number) == 10):
            find_by_number(number)
        else:
            print("This is invalid number")
            number = input("What the number you want to search? ")
    elif(int(choice) == 2):
        name = input('what is the name? ')
        find_by_name(name.capitalize())
    elif(int(choice) == 3):
        name = input('What is the name of the new contact? ')
        number = input("what is the number? ")
        if name not in phone_numbers['names']:
            name = name.capitalize()
            inser_number(name,number)
        else:
            print(name , " is alerday in the phone book")
    elif(int(choice) == 4):
        print_all_number()
    elif(int(choice) == 5):
        flag = False

    else:
        print("This invalid number")
