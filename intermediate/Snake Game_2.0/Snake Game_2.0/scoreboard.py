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
        try:
            with open('data.txt') as data:
                self.high_score = int(data.read())
        except:
            self.high_score = 0
        #在 Score 类初始化时尝试从 data.txt 文件中读取之前的最高分。
        # 如果文件不存在或内容无法读取（例如文件为空或包含非整数值），则将 high_score 初始化为 0。
        self.scoreboard_update()

        
        
    def scoreboard_update(self):
        self.clear()
        self.write(f'Score:{self.score} High Score:{self.high_score}',
                   align=FONT,font=ALIGNMENT)
        
    
# =============================================================================
#     def game_over(self):
#         self.goto(0,0)
#         self.write('GAME OVER', align=FONT,font=ALIGNMENT)
# =============================================================================
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.scoreboard_update()
        
    def score_refresh(self):
        self.score += 1
        self.scoreboard_update()
        
    def game_over(self):
        if input('Countinue Challenging? Yes/No:\n').lower()=='yes':
            return False
        else:
            return True
        
