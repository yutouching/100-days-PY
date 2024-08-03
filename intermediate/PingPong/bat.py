from turtle import Turtle


MOVE_DISTANCE = 30
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)#形状拉伸，倍率
        self.penup()
        self.goto(position)            #移到屏幕边缘
    
    
    
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
