import colorgram as cg
import turtle as tl
import random

#%%提取颜色list
colors = cg.extract('Hirst spot painting .jpg', 30)
color_rgb = []
for i in colors:
    #将复杂的rbg输出改成纯tuple数字的list(纯元组)
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r,g,b)
    color_rgb.append(new_color)
    
#先打印出结果，删掉可能是白色阴影的数值，重新写一个有效的list。不过我懒得删就这样吧
#%%

#初始设置
tl.colormode(255)
mbappe = tl.Turtle()
mbappe.speed('fastest')
num_dot = 100

#确定初始位置：
mbappe.penup()
mbappe.hideturtle()
mbappe.setheading(225)
mbappe.forward(300)
mbappe.setheading(0)


for dot in range(1, num_dot + 1):
    mbappe.pendown()
    mbappe.dot(20,random.choice(color_rgb))
    mbappe.penup()
    mbappe.forward(50)
    
    if dot % 10 == 0:        #换行
        mbappe.setheading(90)
        mbappe.forward(50)
        mbappe.setheading(180)
        mbappe.forward(500)
        mbappe.setheading(0)
        










screen = tl.Screen()
screen.exitonclick()

