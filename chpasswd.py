#!/usr/bin/python3

import os
import string
import random

def generator_password(length_password):
    all_symbols = string.ascii_letters + string.digits + string.punctuation

    condition = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
                 random.choice(string.digits), random.choice(string.punctuation)]

    password = random.sample(condition, len(condition)) + random.sample(all_symbols, length_password - len(condition))

    random.shuffle(password)

    return ''.join(password)

def search_pass_user(user):
    word = f"{user}:!:"

    with open("/etc/shadow", "r") as file:
        content = file.read()
        if word in content:
            return 0
        else:
            return 1


user_name = input("Enter your username: ")

check_exist_user = os.system(f'id {user_name}')

if check_exist_user != 0:
    print("Error: enter valid username !!!")
else:
    print(f"Congratulations!!! {user_name} are in system !")

    check_exist_password = search_pass_user(user_name)
    if check_exist_password == 0:
        print("You do not have a password yet !!!")
        user_choice_with_no_password = input("If you want to generate and set password to your account, please enter 'yes': ")
        if user_choice_with_no_password == 'yes':
            length_password_for_user_with_no_password = int(input("Please enter length password: "))
            password = generator_password(length_password_for_user_with_no_password)
            print(f"Your password: {password}")
        else:
            exit()
    else:
        print("Good !!! Password already exists !")
        user_choice_with_password = input("If you want to generate and set new password to your account, please enter 'yes': ")
        if user_choice_with_password == 'yes':
            length_password_for_user_with_password = int(input("Please enter length password: "))
            password = generator_password(length_password_for_user_with_password)
            print(f"Your password: {password}")
        else:
            exit()
