'''game finding a secret number within 3 attempts using while loop'''
import random
randomNo = random.randint(0, 9)
guessNo = int(input('Guess a number from 0 to 9 : '))
attempt = 1
while randomNo != guessNo:
    if attempt <= 2:
        guessNo = int(input('Guess again : '))
    else:
        print("Sorry ! you've reached your limitation.")
        break
    attempt += 1
if guessNo == randomNo:
    print("Congratulations! You've found the secret number.")