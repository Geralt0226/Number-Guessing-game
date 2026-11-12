#Guessing game with 3 tries only

right_number = 6
tries = 3

while tries > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == right_number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Sorry, Wrong number.")
        tries -= 1
else:
    print("You've run out of tries. The number was", right_number)




