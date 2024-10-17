print("Hello to Milan's Pizza Delivery!")

# Get user input for pizza size and extras
size = input("Which size do you want? S, M, or L: ").upper()  # Convert to uppercase for uniformity
peperoni = input("Do you want extra pepperoni on your pizza? Y for yes, N for no: ").upper()
cheese = input("Do you want extra cheese? Y for yes, N for no: ").upper()

# Initialize bill
bill = 0

# Calculate the base cost based on the size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size entered!")

# Add the cost of extra pepperoni
if peperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add the cost of extra cheese
if cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your total bill is: ${bill}")

