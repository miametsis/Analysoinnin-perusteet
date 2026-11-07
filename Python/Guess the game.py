name = "Mia"

guess = input(" Guess the game: ")

while guess != name:
    print("Wrong! Try again.")
    guess = input("Guess the name:")
print("Congratulation!")

name = " Mia"
guesses = 0 
guesses = input(" Guess the name: ")
guesses = guesses + 1

while guess != name:
    answer = input("Wrong! Quit? (Yes or no):")
    if answer == "yes":
        break
    guess = input("Guess again:")
    guesses = guesses +1

    if guesses == name:
        print("Congratulation!")
        print("You guessed", guesses, "times.")
    else:
        print("Game over.")