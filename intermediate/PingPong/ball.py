from turtle import Turtle
import random
import math

INIT_SPEED = 3

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = INIT_SPEED
        self.reset_direction()  # 初始化方向和速度
        
        
    def move(self):
        
        new_x = self.xcor() + self.x_angle * self.move_speed
        new_y = self.ycor() + self.y_angle * self.move_speed
        self.goto(new_x, new_y)
        
    
    def bounce_y(self):    #上下边界反弹设置，直接用y数值的相反数。即对称反弹。
        self.y_angle *= -1
    
    def bounce_x(self):     #球拍反弹设置。x数值反弹。
        self.x_angle *= -1
        self.move_speed *= 1.1
        
    def reset_direction(self):
    # 生成-π/4到π/4或3π/4到5π/4的随机角度
        if random.choice([True, False]):    #随机True or False
            angle = random.uniform(-math.pi/3, math.pi/3)  #右
        else:
            angle = random.uniform(2*math.pi/3, 4*math.pi/3)#左
        
        self.x_angle = math.cos(angle)  # 计算x方向速度分量（单位向量）
        self.y_angle = math.sin(angle)  # 计算y方向速度分量（单位向量）
        self.move_speed = INIT_SPEED


    def reposition(self):
        self.goto(0,0)
        self.reset_direction()  # 重置方向和速度
        self.move()