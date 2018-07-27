# THIS IS A SIMPLE ADDITION AND SUBTRACTION PROGRAM

import random

# Input a name
print('\nHello! This is AddOrSubt app.\n')
print('Please enter your name:')
name = input()
print('\nHi %s!' % name.capitalize())

# Select A. Addition or B. Subtraction
while True:
    print('Choose one (Click A or B): \nA. Addition\nB. Subtraction')
    program_choice = input().lower()

    def addition(num1, num2):  
        sum = num1 + num2
        print('\nAnswer: ' + str(num1) + ' plus ' + str(num2) + ' is ' + str(sum) + '!')

    def subtraction(num1, num2):
        difference = num1 - num2
        print('\nAnswer: ' + str(num1) + ' minus ' + str(num2) + ' is ' + str(difference) + '!')

    if program_choice == 'a':
        while True:
            print('\nEnter a number:')
            try:
                num1 = int(input()) 
                print('\n%s plus ...?' % str(num1))
                num2 = int(input())
                addition(num1, num2)
                break
            except ValueError:
                print('Please enter an integer!')
    elif program_choice == 'b':
        while True:
            print('\nEnter a number:')
            try:
                num1 = int(input())
                print('\n%s minus ...?' % str(num1))
                num2 = int(input())
                subtraction(num1, num2)
                break
            except ValueError:
                print('Please enter an integer!')
    else:
        print('\nClick A or B only.\n')
        continue

    # Print a random supportive word when player replay and thank you when player exits
    supportWords = ['Great!', 'Nice!', 'Okay let\'s!', 'Let\'s go!', 'Awesome!', 'Okay, be fast!']
    print('\nClick Enter to replay (or E to exit):')
    replay_choice = input().lower()

    if replay_choice == '':
        print(supportWords[random.randint(0, len(supportWords))])
        continue
    elif replay_choice == 'e':
        print('Thank you. Program exits.')
        break
    else:
        print('Click enter or C')