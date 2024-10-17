import random
from replit import clear

def generate_numbers():
    random_numbers = random.sample(range(1, 48), 6)
    random_numbers.sort()
    return random_numbers
  
clear()
random_numbers = generate_numbers()
print ('Your Lackey Six numbers are:')
print(" ".join(str(number) for number in random_numbers))


while True:
    play_again = input("Do you want a new numbers (yes/no)? ").lower()
    if play_again == "no":
        clear()
        break
    elif play_again == "yes":
        clear()
        random_numbers = generate_numbers()
        print ('Your Lackey Six numbers are:')
        print(" ".join(str(number) for number in random_numbers))
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
       