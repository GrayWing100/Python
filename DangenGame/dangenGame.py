print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
a = input("Choose left or right").lower()

if a == "left":
 b = input("You came to the beach, do you gonna Wait for boat or Swim the river." ).lower()
 if b == "wait":
    c =  input("Choose the door: Blue, Red or Yellow." ).lower()
    if c == "yellow":
        print("Cave man eat u!")
    elif c == "blue":
        print("You find  the gold.")
    elif c == "red":
        print ("Dragon eat u!")
    else:
       prin ("Try again!")
 else:
    print("Shark eat you. Game Over.")
else:
    print("You are DEAD.")
