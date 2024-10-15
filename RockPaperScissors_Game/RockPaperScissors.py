import random
from gameImages import game_images

# Get player's input
playerAnswer = int(input("Hi, let's play Rock, Paper, and Scissors!\nType 0 for Rock, 1 for Paper, and 2 for Scissors:\n"))

if playerAnswer >= 3 or playerAnswer < 0:
    print("Error! You typed an invalid number!")
else:
    print(game_images[playerAnswer])

    # Computer randomly selects Rock, Paper, or Scissors
    computerAnswer = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computerAnswer])

    # Determine the outcome of the game
    if playerAnswer == 0 and computerAnswer == 2:
        print("You won the game!")
    elif computerAnswer == 0 and playerAnswer == 2:
        print("You lost the game!")
    elif computerAnswer > playerAnswer:
        print("You lost the game!")
    elif playerAnswer > computerAnswer:
        print("You won the game!")
    elif playerAnswer == computerAnswer:
        print("It's a draw!")    


