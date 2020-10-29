# Integer Guessing Game

from random import randint
num = randint(1, 100)

print("[+] Guessing Game")
print('''\nThe program will generate a random number between 1 and 100 and you have to GUESS it.
The program will tell you how warm or cold you are based on your guesses.
There no limit to the number of guesses.
Type your guesses in the input bar.
Only integers are allowed.''')

guess_list = []
guess = int(input("Enter your First GUESS: "))

while(guess != num):
    if(len(guess_list) == 0):
        if(abs(guess-num) <= 10):
            print("Warm!")
        elif(abs(guess-num) > 10):
            print("Cold!")
        guess_list.append(guess)
    elif(1 > guess and guess > 100):
        print("Out of Bounds!")
    elif(len(guess_list) != 0):
        if(abs(num-guess_list[-1]) > abs(num-guess)):
            print("Warmer!")
        elif(abs(num-guess_list[-1]) < abs(num-guess)):
            print("Colder!")
        guess_list.append(guess)

    guess = int(input("Enter your next GUESS: "))

else:
    a = len(guess_list)
    print("Bingo!!! It took you {} tries to get it right.".format(a))
    guess_list.append(guess)
    
