from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_sine_n in range(3, 11):
    draw_shape(shape_sine_n)

screen = Screen()
screen.exitonclick()
