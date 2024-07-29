#Etch-A-Sketch-App

import turtle as tl

mbappe = tl.Turtle()
screen = tl.Screen()

def move_forward():
    mbappe.forward(10)
    
def move_backward():
    mbappe.backward(10)
    
def turn_left():
    mbappe.left(10)

def turn_right():
    mbappe.right(10)

def clear():
    mbappe.clear()
    mbappe.penup()
    mbappe.home()
    mbappe.pendown()

#%%Etch-A-Sketch-App
screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')






screen.exitonclick()


