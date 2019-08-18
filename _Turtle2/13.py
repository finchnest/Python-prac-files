from turtle import Turtle
def rec(length,color):
    bob = Turtle()
    bob.color(color)
    bob.forward(length)
    bob.right(90)
    bob.forward(length)
    bob.right(90)
    bob.forward(length)
    bob.right(90)
    bob.forward(length)



rec(100,'red')
