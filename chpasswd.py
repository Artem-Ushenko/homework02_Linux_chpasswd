#!/usr/bin/python3

import os


user_name = input("Enter your username: ")

check_exist_user = os.system(f'id {user_name}')

if check_exist_user != 0:
    print("Error: enter valid username !!!")
else:
    print(f"Congratulations!!! {user_name} are in system !")

    check_exist_password = os.system(f'cat /etc/shadow | grep {user_name}:*:')
    print(check_exist_password)
    if check_exist_password == 0:
        print("You do not have a password yet !!!")
        user_choice_with_no_password = input("If you want to generate and set password to your account, please enter 'yes': ")
        if user_choice_with_no_password == 'yes':
            print('generate and set password')
        else:
            print('Password are not set in your account !!!')
            exit()
    else:
        print("Good !!! Password already exists !")
        user_choice_with_password = input("If you want to generate and set new password to your account, please enter 'yes': ")
        if user_choice_with_password == 'yes':
            print("generate and set new password")
        else:
            print("You already have a password. We recommend to change it !!!")
