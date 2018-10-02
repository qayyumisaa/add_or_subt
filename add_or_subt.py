# THIS IS A SIMPLE ADDITION AND SUBTRACTION PROGRAM

import random

def addition(num1, num2):  
    sum = num1 + num2
    print('\nAnswer: ' + str(num1) + ' plus ' + str(num2) + ' is ' + str(sum) + '!')

def subtraction(num1, num2):
    difference = num1 - num2
    print('\nAnswer: ' + str(num1) + ' minus ' + str(num2) + ' is ' + str(difference) + '!')


# Input a name
print('\nHello! This is AddOrSubt app.\n')
name = input('Please enter your name: ')
print('\nHi %s!' % name.capitalize())

# Select A. Addition or B. Subtraction
while True:
    program_choice = input('Choose one (Click A or B): \nA. Addition\nB. Subtraction').lower().strip()

    if program_choice == 'a':
        while True:
            try:
                num1 = int(input('\nEnter a number: '))
                num2 = int(input('\n%s plus ...?' % str(num1)))
                addition(num1, num2)
                break
            except ValueError:
                print('Please enter an integer!')

    elif program_choice == 'b':
        while True:
            try:
                num1 = int(input('\nEnter a number: '))
                num2 = int(input('\n%s minus ...?' % str(num1)))
                subtraction(num1, num2)
                break
            except ValueError:
                print('Please enter an integer!')

    else:
        print('\nClick A or B only.\n')
        continue

    # Print a random supportive word when player replay and thank you when player exits
    supportWords = ['Great!', 'Nice!', 'Okay let\'s!', 'Let\'s go!', 'Awesome!', 'Okay, be fast!']
    replay_choice = input('\nClick Enter to replay (or E to exit): ').lower().strip()

    if replay_choice == 'e':
        print('Thank you. Program exits.')
        break

    if replay_choice == '':
        print(supportWords[random.randint(0, len(supportWords))])
        continue
        
    print('Click enter or C')