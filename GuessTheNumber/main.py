import random
#from art import logo

#print(logo)
print("Welcome to number gessing game! ")
print("I'm thinking of a number between 1 and 100.")

def guessing_game():
    # choose a random number between 1 and 100
    number = random.randint(1, 100)

    # get the number of lives based on the chosen level
    level = input("Choose your level (easy/hard): ")
    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5
    else:
        print("Invalid level selection!")
        return

    # loop to allow the player to guess the number
    while lives > 0:
        guess = int(input("Guess a number between 1 and 100: "))

        # check if the guess is correct
        if guess == number:
            print("Congratulations! You guessed the number.")
            return
        # give feedback to the player and update the number of lives
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")
        lives -= 1
        print("Lives remaining:", lives)

    # if the player runs out of lives, reveal the number and end the game
    print("Sorry, you ran out of lives. The number was", number)

guessing_game()
