import random

while True:
    choices = ['R', 'P', 'S']
    computer_choice = random.choice(choices)
    user_choice = input("Select your Choice; 'R' for Rock, 'P' for Paper, 'S' for Scissors: ")

    while user_choice not in choices:
        print('Invallid choice, check the options and chose from it!') 
        choices = ['R', 'P', 'S']
        computer_choice = random.choice(choices)
        user_choice = input("Select your Choice; 'R' for Rock, 'P' for Paper, 'S' for Scissors: ")
        
    while user_choice == computer_choice:
        print(f"Computer Selected {computer_choice} and You also Selected {user_choice}. it's a tie!")
        choices = ['R', 'P', 'S']
        computer_choice = random.choice(choices)
        user_choice = input("Select your Choice; 'R' for Rock, 'P' for Paper, 'S' for Scissors: ")
    
    if user_choice == 'R' : #or 'r':
        if computer_choice == 'S' : #or 's'
            print('You chose', user_choice)
            print('computer chose', computer_choice)
            print('Rock Smashes Scissors! You Won!')
        else:
            print('You chose', user_choice)
            print('computer chose', computer_choice)
            print('paper covers rock! you lose.')

    
    elif user_choice == 'P' : #or 'p'
        if computer_choice == 'R' : #or 'r':
            print('You chose', user_choice)
            print('computer chose', computer_choice)
            print('Paper Covers Rock! You won!')
        else:
            print('You chose', user_choice)
            print('computer chose', computer_choice)
            print('scissors cuts paper! You lose')

    
    elif user_choice == 'S' : #or 's':
        if computer_choice == 'P' : #or 'p':
            print('You chose', user_choice)
            print('computer chose', computer_choice)
            print('Scissors cuts Paper! You won')
        else:
            print('You chose', user_choice)
            print('computer chose', computer_choice)
            print('Rock Smashes Scissors! You lose!')
    play_again = input('play again? (y/n): ')
    if play_again.lower() != 'y':
        break