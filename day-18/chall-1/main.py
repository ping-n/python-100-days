#####Turtle Intro######

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

######## Challenge 1 - Draw a Square ############

for _ in range(4):
    tim.forward(100)
    tim.left(90)
