# Import the custom module
import another_module

# Print the value of another_variable from another_module
print(another_module.another_variable)  # This will print 12

# Working with Turtle module
from turtle import Turtle, Screen

# Create a turtle object and customize it
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("purple")  # Corrected spelling of 'purple'
timmy.forward(100)

# Create a screen object
my_screen = Screen()

# Print the canvas width of the screen
print(my_screen.canvwidth)

# Wait for a click to close the window
my_screen.exitonclick()
