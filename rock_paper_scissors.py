import random 

emojis={'r': '🪨', 's': '✂️', 'p':'📜'}
choices= ('r','p','s')

def get_user_choice():
  while True:
    choice= input('Rock, Paper, Scissors (r/p/s): ').lower()
    if choice in choices:
     return choice
    else:
     print('Invalid Choice!')

def display_choices(choice, computer_choice):
   print(f'You chose {emojis[choice]}')
   print(f'The computer chose {emojis[computer_choice]}')

def determine_the_winner(choice, computer_choice):
    if choice == computer_choice:
        print('Tie!')
    elif (
    (choice=='r' and computer_choice=='s') or 
    (choice=='s' and computer_choice=='p') or 
    (choice=='p' and computer_choice=='r')):
        print('You win!')    
    else :
        print('You lose!')   

    def play_game():
      while True:
        choice= get_user_choice()
        computer_choice= random.choice(choices)  
        display_choices(choice, computer_choice)
        determine_the_winner(choice, computer_choice)
        want_continue= input('Continue? (y/n): ') .lower() 
        if want_continue=='n':
             break   