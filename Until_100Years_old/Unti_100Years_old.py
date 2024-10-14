from datetime import datetime

print("Welcome, this program calculates how many years you have left until you turn 100.")
print("Please enter your date of birth, down below.")

# Get the user day of birth
year_of_birth = int(input("Please enter year of birth: "))
month_of_birth = int(input("Moth: "))
day_of_birth= int(input("And day of birth: "))

#Get the current year, month, and day
current_date = datetime.now()

# Calculate age
birth_date = datetime(year_of_birth, month_of_birth, day_of_birth)
age = (current_date - birth_date).days // 365  # approximate age in years

# Calculate years left to 100
years_left = 100 - age

# If the birthdate hasn't occurred yet this year, subtract 1 from the years left
if (current_date.month, current_date.day) < (month_of_birth, day_of_birth):
    years_left -= 1

# Calculate months and days left for the next birthday
if (current_date.month, current_date.day) >= (month_of_birth, day_of_birth):
    next_birthday_year = current_date.year + 1  # If the birthday has already occurred this year, set next year
else:
    next_birthday_year = current_date.year  # If the birthday is yet to come, use this year

# Create the next birthday datetime object
next_birthday = datetime(next_birthday_year, month_of_birth, day_of_birth)
# second  vay to write a next_birtday
# next_birthday = datetime(current_date.year + (1 if (current_date.month, current_date.day) >= (month_of_birth, day_of_birth) else 0), month_of_birth, day_of_birth)

remaining_days = (next_birthday - current_date).days

# Output the result
print(f"You have {years_left} years and {remaining_days % 365} days left until you are 100 years old.")
