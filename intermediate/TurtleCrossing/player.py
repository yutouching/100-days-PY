STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape('turtle')
        self.penup()
        self.at_start()
        self.setheading(90)
        
        
    def up(self):
        self.forward(MOVE_DISTANCE)
        
    
    def at_end(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    
    def at_start(self):
        self.goto(STARTING_POSITION)
        