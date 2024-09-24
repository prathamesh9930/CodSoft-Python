    #Creating a Rock Paper Scissors game...

import random
computer = random.choice([1, 2, 3])  # 1 = Rock, 2 = Paper, 3 = Scissors
youint = input('Enter your choice: ')
my_dict = {'r': 1, 'p': 2, 's': 3}  # 1 = Rock, 2 = Paper, 3 = Scissors
shortdict = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
you = my_dict[youint]

print('You chose:', shortdict[you])
print('Computer chose:', shortdict[computer])

if (computer == you):
    print('It is a tie!')
else:
    if(you == 1 and computer == 3):
        print('You win!')
    elif(you == 1 and computer == 2):
        print('You lose!')
    elif(you == 2 and computer == 1):
        print('You win!')
    elif(you == 3 and computer == 1):
        print('You lose!')
    elif(you == 2 and computer == 3):
        print('You lose!')
    elif(you == 3 and computer == 2):
        print('You win!')
    else:
        print('Invalid input! You have not entered rock, paper or scissors')