from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = random.random()
        self.y_move = random.random()
        self.move_speed = 0.01
        
        
    def move(self):
        
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    
    def bounce_y(self):    #上下边界反弹设置，直接用y数值的相反数。即对称反弹。
        self.y_move *= -1
    
    def bounce_x(self):     #球拍反弹设置。x数值反弹。
        self.x_move *= -1
        
    def reposition(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.move() 
        