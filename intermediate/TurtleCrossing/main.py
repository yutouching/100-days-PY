import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor('white')
screen.title('TurtleCorss')


turtle = Player()
car = CarManager()
scoreboard = Scoreboard()


#乌龟按键交互
screen.listen()
screen.onkey(turtle.up, 'space')



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # generate car
    car.generate_car()
    car.move_car()
    
    #collides with the cars
    for i in car.all_cars:
        if i.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
            
            
    #collides with boundary
    if turtle.at_end():
        turtle.at_start()         
        car.level_up()
        scoreboard.score_refresh()



screen.exitonclick()