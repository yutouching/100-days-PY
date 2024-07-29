import turtle as tl
import random

is_race_on = False
#%%窗口基础设置
screen = tl.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter a color:')

#%%instance基础设置：
y_position = [100,50,0,-50,-100]
colors = ['red','yellow','blue','green','black']
all_turtle = []


for turtle in range(5):
    mbappe = tl.Turtle()
    mbappe.penup()
    mbappe.goto(x=-230,y=y_position[turtle])
    mbappe.shape('turtle')
    mbappe.color(colors[turtle])
    all_turtle.append(mbappe)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        
        if turtle.xcor()>230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f'You won! The {user_bet} is the winner.')
            else:
                print(f'You lose! The {turtle.pencolor()} turtle is the winner.')
            break
                
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)
        

screen.exitonclick()