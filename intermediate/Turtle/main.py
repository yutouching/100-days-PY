"""
文档（document）对要import的数据/包的内容解释，可以详细到每一个功能
"""
#from modual import *   从包中导入所有内容。不常用，因为会影响可读性
from turtle import Turtle, Screen
import random

mbappe = Turtle()
mbappe.screen.colormode(255) #加载RGB的使用方式：255/1
mbappe.shape('turtle')
mbappe.color('red')#可以根据TK color（TKinter）额名称来更改颜色

#for _ in range(4):         #重复执行4次  正方形
#    mbappe.forward(100)
#    mbappe.right(90)

# =============================================================================
# for _ in range(50):        虚线
#     mbappe.forward(10)
#     mbappe.penup()
#     mbappe.forward(10)
#     mbappe.pendown()
# =============================================================================
# =============================================================================
# for line in range(3,11):    多边形绘图
#     a = 360/line
#     for _ in range(line):
#         mbappe.forward(100)
#         mbappe.left(a)
# =============================================================================
COLORS  =['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 
          'old lace','linen', 'antique white', 'papaya whip',
          'blanched almond', 'bisque', 'peach puff','navajo white', 
          'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
          'slate gray','light slate gray', 'gray', 'light grey',
          'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue',
          'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue',
          'light sky blue', 'steel blue', 'light steel blue','light blue',
          'powder blue', 'pale turquoise', 'dark turquoise',
          'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue',
          'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green',
          'pale green', 'spring green','lawn green', 'medium spring green',
          'green yellow', 'lime green', 'yellow green','forest green',
          'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
          'light goldenrod yellow','light yellow', 'yellow', 'gold',
          'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon',
          'light salmon', 'orange', 'dark orange','coral', 'light coral',
          'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink',
          'light pink','pale violet red', 'maroon', 'medium violet red',
          'violet red','medium orchid', 'dark orchid', 'dark violet',
          'blue violet', 'purple', 'medium purple','thistle']


def color():
    return random.choice(COLORS)

DIRECTION = [0, 90, 180, 270]
def direction():
    return random.choice(DIRECTION)

def RGB():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb
# =============================================================================
#%%random walk
# mbappe.pensize(15)          #笔画粗细
# mbappe.speed('fastest')    #作画速度
# for _ in range(100):
#     mbappe.left(direction())
# #    mbappe.color(color())           #list随机颜色
#     mbappe.color(RGB())               #RBG随机颜色
#     mbappe.forward(50)
# =============================================================================
    
#%%circle
mbappe.speed('fastest')
angle = 6
repeat_times = int(360/angle)
for _ in range(repeat_times):
    mbappe.color(RGB())
    mbappe.circle(100)
    mbappe.left(angle)
#改方向其他方法：
#current_heading = mbappe.heading()       定位乌龟现在的方向
#mbappe.setheading(current_heading+10     转向（重新设置方向）




screen = Screen()
screen.exitonclick()  #保持图片窗口弹出直到点击屏幕
