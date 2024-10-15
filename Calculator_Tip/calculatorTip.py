print("Hi and welcome to my tip-calculator!")

# Get input values from the user
bill = float(input("Write total bill: $"))
people = int(input("How many people: "))
percentageTip = int(input("Tip percentage: %"))

# Calculate the total tip and the amount each person should pay
tip = (100 + percentageTip) / 100
eachBill = round((bill / people) * tip, 2)

# Display the result
print(f"Each person should pay: ${eachBill}")
