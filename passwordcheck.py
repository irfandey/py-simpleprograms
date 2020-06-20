import re

def password_check():
    value = 0
    password = input("Input password = ")
    if re.search('[a-z]', password):
        value = value + 1
    if re.search('[A-Z]', password):
        value = value + 1
    if re.search('[0-9]', password):
        value = value + 1
    if re.search('[!@#$%^&*()~_+":?><.,;=-]', password):
        value = value + 1
    if len(password) < 8:
        print("The password should have more than 8 characters")
    if value == 4:
        print("Strong Password")
    if value == 3:
        print("Medium Password")
    if value == 2:
        print("Weak Password")
    if value == 1:
        print("Very Weak Password")
    return 0

password_check()
