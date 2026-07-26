import random 

numbe= random.randint(1,100)

while True:
    try:
     guess= int(input('Guess the number between 1 and 100: '))
    except ValueError:
       print('Please Enter a valid number')

       