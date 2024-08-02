from turtle import Turtle

FONT = 'center'
ALIGNMENT = ('Arial',24,'normal')




class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        
        self.score = 0
        self.scoreboard_update()

        
        
    def scoreboard_update(self):
        self.clear()
        self.write(f'Score:{self.score}', align=FONT,font=ALIGNMENT)
        
    
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=FONT,font=ALIGNMENT)
        
        
    def score_refresh(self):
        self.score += 1
        self.scoreboard_update()
        
