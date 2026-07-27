import random 

emojis={'r': '🪨', 's': '✂️', 'p':'📜'}
choices= ('r','p','s')

while True:
    choice= input('Rock, Paper, Scissors (r/p/s): ').lower()
    if choice not in choices:
        print('Invalid choice!')
        continue

    computer_choice= random.choice(choices)    

    print(f'You chose {emojis[choice]}')
    print(f'The computer chose {emojis[computer_choice]}')

    if choice == computer_choice:
        print('Tie!')
    elif (
    (choice=='r' and computer_choice=='s') or 
    (choice=='s' and computer_choice=='p') or 
    (choice=='p' and computer_choice=='r')):
        print('You win!')    
    else :
        print('You lose!')   

    want_continue= input('Continue? (y/n): ') .lower() 
    if want_continue=='n':
        break   