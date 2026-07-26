import random 

emojis={'r': '🪨', 's': '✂️', 'p':'📜'}
choices= ('r','p','s')
choice= input('Rock, Paper, Scissors (r/p/s): ').lower()
if choice not in choices:
    print('Invalid choice!')
computer_choice= random.choice(choices)    
print(f'You chose {emojis[choice]}')
print(f'The computer chose {emojis[computer_choice]}')
