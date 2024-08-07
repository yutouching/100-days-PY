from turtle import Turtle
import random



class Food(Turtle):           #继承了Turtle class   inheritance
    
    def __init__(self):
        super().__init__()   #继承步骤。不必要。此时food已经继承了Turtle的attribute
        
        self.shape('circle') #因为继承，可以直接用self导出shape功能
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        #默认20*20pixel。0.5为倍率
        self.color('green')
        self.speed('fastest')
        self.food_refresh()
        
        
    def food_refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
