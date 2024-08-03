import turtle as tl
from bat import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = tl.Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('PingPong')

screen.tracer(0)

#三个实体
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()

screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')

screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard = Scoreboard()
    
    # 检测上下边界
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
        
    #检测球和球拍的碰撞
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() <-325:
        ball.bounce_x()
        
        ball.move_speed *= 0.9#接到球后球速变快，难度增加
        
    
    #检测接不到球, 失球和分数变化
    if ball.xcor() > 380:   #检测边界。右边失球，左边得分
        scoreboard.l_point()    #分数变更
        scoreboard.update_score()   #刷新面板
        ball.reposition()   #重新发球
        
        
    if ball.xcor() < -380:
        scoreboard.r_point()    
        scoreboard.update_score() 
        ball.reposition()    #重新发球。重置位置、方向、球速
        
        












screen.exitonclick()
