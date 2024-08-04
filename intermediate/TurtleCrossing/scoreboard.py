FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-280,250)
        self.update_scoreboard()    
        
        
        
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',align='center', font=FONT)
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'Level:{self.level}',align='left',font=FONT)
        
    def score_refresh(self):
        self.level += 1
        self.update_scoreboard()    
        
    
        
