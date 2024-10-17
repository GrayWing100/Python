import random
import hm_art
import hm_words
from hm_art import stages, logo, logo_two
from hm_words import word_list

def play_game():
    end_of_game = False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 7

    display = []
    missed_letters = []
    for _ in range(word_length):
        display += "_"

    print(logo)
    print(f"{', '.join(display)} {word_length} words guess.")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        
        # Simulate clearing the screen
        print("\n" * 100)

        if guess in display or guess in missed_letters:
            print(f"You've already guessed {guess}.")
            continue

        correct_guess = False
        for position in range(word_length):
            letter = chosen_word[position]
        
            if letter == guess:
                display[position] = letter
    
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            missed_letters.append(guess)
            if lives == 0:
                end_of_game = True
                print(f"You lose! The word is {chosen_word}, try again.")
        
        print(f"{'  '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win!")

        print(stages[lives])
        print(f"Used words: {', '.join(missed_letters)}")

while True:
    play_game()
    play_again = input("Do you want to play again (yes/no)? ").lower()
    if play_again == "no":
        print("See you later!")
        #print(logo_two)
        break
    else:
        print("\n" * 100)
