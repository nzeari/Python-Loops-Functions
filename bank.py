database = {}

import time

t = time.asctime()

import random


def choice2():
    print('Would you like to perform another transaction?')
    print('1. No')
    print('2. Yes')
    choosenOption2 = int(input('Please choose an option \n'))

    if (choosenOption2 == 1):
        print('Goodbye and have a nice day')
        exit

    elif (choosenOption2 == 2):
        choice1()

    else:
        print('Invalid option selected, kindly try again')


def choice1():
    print('What would you like to do?')
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Complaints')
    choosenOption1 = int(input('Please choose an option \n'))
    if (choosenOption1 == 1):
        current_balance = 500000
        withdrawal_amount = int(input('How much would you like to withdraw \n'))
        withdrawable_amount = current_balance - withdrawal_amount
        print("Please take your cash")

    elif (choosenOption1 == 2):
        current_balance = 500000
        deposit_amount = int(input('How much would you like to deposit \n'))
        current_balance = deposit_amount + previous_balance
        print("Your current balance is")

    elif (choosenOption1 == 3):
        print(input('What issue will you like to report? \n'))
        print("Thank you for banking with us")

    else:
        print('Invalid option selected, kindly try again')


def login():
    UserAccountNumber = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    if (databaseUserAccountNumber == UserAccountNumber):
        if (databasePassword == password):
            print('Welcome')


def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


def register():
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    print('Password successfully created')
    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created")

    print("Your account number is: %d" % accountNumber)
    print("Your account number would be sent to your email.")


print('Welcome to GTB, today is', t)
print("Do you have account with us?")
print("1. Yes")
print("2. No")

selectOption = int(input("Select an option \n"))

if (selectOption == 1):
    login()
elif (selectOption == 2):
    register()
    generationAccountNumber()

    choice1()

    choice2()




else:
    print("You have selected an invalid option")
    login()
