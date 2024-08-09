from email.mime import image
import turtle
import pandas as pd

#Constant
GUESSNUMBER = 50


#Screen Setup
screen = turtle.Screen()
screen.title('U.S. State Game')

#load the map image
state_image = 'blank_states_img.gif'
screen.addshape(state_image)
turtle.shape(state_image)

#导入文件
data = pd.read_csv('50_states.csv')
all_state = data['state'].to_list()             #将某一列转成列表




#main loop
guess_state = []
while len(guess_state) < GUESSNUMBER:

    #统一大小写
    answer_state = screen.textinput(title=f'{len(guess_state)}/{GUESSNUMBER} State Correct',
                                    prompt = 'What is another state name?').title()


    if answer_state is None or answer_state == 'Exit':
        miss_state = []
        for state in all_state:
            miss_state.append(state)

        miss_file = pd.DataFrame(miss_state)
        miss_file.to_csv('state_to_learn.csv')

        break 
    
    if answer_state in all_state and answer_state not in guess_state:
        guess_state.append(answer_state)
        #创造一个turtle来写出州名
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()

        location = data[data['state'] == answer_state] #定位写出的州的方位。此处是series
        #location = data[data.state == answer_state]
        #data['state']==answer_state 和 data.state == answer_state等价

        pen.goto(location.x.item(),location.y.item())#定位到series的具体item
        pen.write(answer_state)

#save missing states and switch them to csv file





# #定位图片地址方式
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)#print点击的坐标
# 不过现在有包就不这么弄了





turtle.mainloop()       #保持界面常开，不因为点击关闭（替代exitonclick）
