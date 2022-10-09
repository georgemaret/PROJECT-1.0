# Rock Paper Scissors
import time
import random

your_score = 0
comp_score = 0

while True:
    print('INSTRUCTIONS:')
    print('-----------------------')
    time.sleep(2)
    print("Press 'R' for Rock")
    print("Press 'P' for Paper")
    print("Press 'S' for Scissors")
    print('-----------------------')

    user_choice = input('Enter your choice here: ')

    state = True
    while state == True:
        if user_choice == 'R' or user_choice == 'r':
            print('You chose Rock!')
            user_choice = 'Rock'
            state = False
        elif user_choice == 'P' or user_choice == 'p':
            print('You chose Paper!')
            user_choice = 'Paper'
            state = False
        elif user_choice == 'S' or user_choice == 's':
            print('You chose Scissors!')
            user_choice = 'Scissors'
            state = False
        else:
            user_choice = input('Enter a valid input: ')
            state = True
    print('Waiting for computer to choose...')
    time.sleep(2)
    comp_choice = random.choice(['Rock','Paper','Scissors'])
    if comp_choice == 'Rock':
        print('Computer chose Rock!')
    if comp_choice == 'Paper':
        print('Computer chose Paper!')
    if comp_choice == 'Scissors':
        print('Computer chose Scissors!')
    print('-----------------------')
    time.sleep(2)
    print(user_choice + ' Vs ' + comp_choice)
    time.sleep(2)
    if user_choice == comp_choice:
        print('GAME TIED!!!')
    if user_choice == 'Rock' and comp_choice == 'Paper':
        print('Paper defeats Rock...')
        print('COMPUTER WINS!!!')
        comp_score+=1
    if user_choice == 'Rock' and comp_choice == 'Scissors':
        print('Rock defeats Scissors...')
        print('YOU WIN!!!')
        your_score+=1
    if  user_choice == 'Paper' and comp_choice == 'Rock':
        print('Paper defeats Rock...')
        print('YOU WIN!!!')
        your_score+=1
    if  user_choice == 'Paper' and comp_choice == 'Scissors':
        print('Scissors defeat Paper...')
        print('COMPUTER WINS!!!')
        comp_score+=1
    if  user_choice == 'Scissors' and comp_choice == 'Rock':
        print('Rock defeats Scissors...')
        print('COMPUTER WINS!!!')
        comp_score+=1
    if  user_choice == 'Scissors' and comp_choice == 'Paper':
        print('Scissors defeat Paper...')
        print('YOU WIN!!!')
        your_score+=1
    print("YOUR SCORE = " + str(your_score))
    print("COMPUTER SCORE = " + str(comp_score))
    wanna_play = input('Do you want to play again?[Y/N] ')
    if wanna_play == 'N' or wanna_play == 'n':
        break

print("FINAL RESULTS")
print("--------------")
print("YOUR SCORE = " + str(your_score))
print("COMPUTER SCORE = " + str(comp_score))
time.sleep(1)
if your_score > comp_score:
    print('YOU WIN THE GAME !!!')
elif your_score < comp_score:
    print('YOU LOSE THE GAME :(')
else:
    print('MATCH TIED !!!')

input('Press Enter key to exit: ')
