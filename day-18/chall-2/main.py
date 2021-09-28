import turtle
from turtle import Turtle
import random

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim = Turtle()
tim.shape("turtle")
tim.color("green", "red")


########### Challenge 2 - Draw dashed line ########

# for _ in range(10):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pd()


########### Challenge 3 - Draw Shapes ########

def draw_shape(side):
    angle = 360 / side
    for _ in range(side):
        tim.forward(70)
        tim.left(angle)


for shape_side in range(3, 10):
    tim.pencolor(random.choice(colors))
    draw_shape(shape_side)
