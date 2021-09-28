import turtle as t
import random

# Setup
direction = [0, 90, 180, 270]
time = 100

# Turtle setup
t.screensize(200, 200)
t.colormode(255)
tim = t.Turtle()
tim.pensize(5)
tim.speed("fastest")
tim.shape("turtle")
tim.color("green", "brown")

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, b, g


def walker():
    tim.forward(30)
    tim.seth(random.choice(direction))
    tim.pencolor(random_color())


for _ in range(time):
    walker()
