import turtle as t
import random

# Setup
direction = [0, 90, 180, 270]
time = 100

# Turtle setup
t.screensize(200, 200)
t.colormode(255)

tim = t.Turtle()
tim.pensize(1)
tim.speed("fastest")
tim.shape("turtle")
tim.color("green", "brown")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + size_of_gap)


draw_circle(10)
t.exitonclick()
