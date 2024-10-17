import random

print("Hi! Welcome to game Name rulette!")

# Get the names from the user
names_string = input("Enter everybody's names, separated by a comma: ")

# Split the names and remove any extra spaces
names = [name.strip() for name in names_string.split(",")]

# Get the total number of people
num_items = len(names)

# Randomly select one person
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

# Display the result
print(f"{person_who_will_pay} is going to buy the meal today!")
