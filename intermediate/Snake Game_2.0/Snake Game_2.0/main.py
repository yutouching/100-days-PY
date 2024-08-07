import turtle as tl
import time
from snake import Snake #此处import的是class
from food import Food
from scoreboard import Score

#%%画面基础设置
screen = tl.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SnakeGame')
screen.tracer(0)        #画面显示追踪器，刚开始关闭。

#%%调用三个实体
snake = Snake()        #调用了__init__的功能，也就是出现三块蛇的基础图像
food = Food()
scoreboard = Score()

#%%按键基础设置
screen.listen()        #将键盘输入与行为function绑定在一起
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')   

#%%主要游戏逻辑
game_is_on = True
print("Game starts")        #调试信息
while game_is_on:
    screen.update()   
    #追踪器更新，开始更新画面。在for外会更新整个蛇的移动，for内则是每个区块
    time.sleep(0.1)   #时间延迟
    
    snake.move()      #此处引用的是function
    
    if snake.head.distance(food) < 15:#检测蛇和食物的距离,吃食物
        print("Food eaten")             #调试信息
        food.food_refresh()             #刷新食物地点
        snake.extend()                  #蛇的身体拓展
        scoreboard.score_refresh()      #分数变化
    
    
    #检测是否撞墙
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Hit the wall")           #调试信息
        if scoreboard.game_over():
            scoreboard.reset()
            game_is_on = False
        else:
            scoreboard.reset()
            snake.reset()
    
    #检测是否撞到尾巴
# =============================================================================
#     for seg in snake.segments:       #第一种方式
#         if seg == snake.head:        #避开蛇头
#             pass
# =============================================================================
    for seg in snake.segments[1:]:     #第二种方式，切片
        if snake.head.distance(seg) < 10: #如果蛇头和身体部分的距离过小（撞了）
            print("Hit itself")         #调试信息
            if scoreboard.game_over():
                scoreboard.reset()
                game_is_on = False
            else:
                scoreboard.reset()
                snake.reset()


print("Game over")                      #调试信息

screen.exitonclick()


