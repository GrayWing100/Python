# Love Calculator Program
print("Welcome to the Love Calculator!")

# Get user input for names
name1 = input("What is your name? \n")
name2 = input("What is the name of your crush? \n")

# Combine the names and convert them to lowercase
combined_names = name1 + name2
lower_names = combined_names.lower()

# Count the occurrences of specific letters for 'TRUE'
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# Count the occurrences of specific letters for 'LOVE'
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Combine the counts to create the score
score = int(str(first_digit) + str(second_digit))

# Determine the result based on the score
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
