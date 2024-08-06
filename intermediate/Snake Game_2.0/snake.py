import turtle as tl

START_POSITION = [(0,0), (-20,0), (-40,0)] #python中常量用大写字母命名   
##因为游戏开始后默认向右直行，确保头部在最右侧！否则会碰撞出错直接导致game over
MOVE_DISTANCE = 20                      #蛇的移动距离。使用变量方便改动
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    
    def __init__(self): #此处为attribute
        
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]


    def creat_snake(self):
        for position in START_POSITION:
            self.add_seg(position)
            print(f"Segment added at {position}") # 调试信息
            
    def add_seg(self, position):
            segment = tl.Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)         
            
    def extend(self):
        self.add_seg(self.segments[-1].position()) #在list的结尾处添加


    def move(self):
# =============================================================================
#     for seg in segments: 通过从头到尾遍历将所有instance（整条蛇）一起往前移
#         seg.forward(20)
# =============================================================================
    #尝试从尾部先开始移动.从1，2，3到3，2，1（为了使所有部分跟着头部转向）
        for seg in range(len(self.segments)-1, 0, -1): #遍历的顺序：(start= , end= , step= )
            new_x = self.segments[seg-1].xcor() #上一个seg，也就是下一步要去的地点坐标
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
    #随后可以通过直接设置segments[0]的行为来控制整个list：例如
        #self.segments[0].forward(MOVE_DISTANCE) #或
    #segments[0].left()
        self.head.forward(MOVE_DISTANCE)
        print(f"Head position: {self.head.position()}")        # 调试信息
        
        
    def reset(self):
        for seg in self.segments:   #将上一把额蛇移出界面
            seg.goto(1000,1000)
        self.segments.clear()        #清除段
        self.creat_snake()
        self.head = self.segments[0]
    
    
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
