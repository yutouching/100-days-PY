#密码生成器：
#载入密码素材库
import string
import numpy as np
letter = list(string.ascii_letters)             #列表类型为string
symbol = ['~','!','@','#','$','%','^','&','*']  #列表类型为string
number = list(range(10))                        #列表里的类型为整数int，在后期拼接中需要调整，不然因为类型不一致会出错

#让用户输入密码需求
print('Welcome to the Password Generator!')
cus_letter = int(input('How many letters would you like in your password?\n'))
cus_symbol = int(input('How many symbols would you like in your password?\n'))
cus_number = int(input('How many numbers would you like in your password?\n'))

#简单版：密码的类型顺序固定
password = ""
for i in range(1,cus_letter+1):              #遍历要求数量的部分密码
    password += np.random.choice(letter)     #将每次遍历生成的单个密码相加
for i in range(1,cus_symbol+1):
    password += np.random.choice(symbol)
for i in range(1,cus_number+1):
    password += str(np.random.choice(number)) #因为数字类型不同，此处将拼接类型统一为string
print(password)

#难版：密码类型顺序不固定
password_list = []
for i in range(1,cus_letter+1):                        #因为i没有被实际使用，所以i也可以改成_ 即for _ in range()
    password_list.append(np.random.choice(letter))     #改成列表元素添加方式。
for i in range(1,cus_symbol+1):
    password_list.append(np.random.choice(symbol))
for i in range(1,cus_number+1):
    password_list.append(str(np.random.choice(number))) 
np.random.shuffle(password_list)                        #打乱顺序，并返回None，因此不需要更新变量 
password_hard = ''.join(password_list)                  #由list拼接成字符串string。
'''
join 是一个字符串方法，它将一个可迭代对象（如列表、元组等）中的所有元素连接成一个字符串，并在每个元素之间插入调用该方法的字符串。
'' 是一个空字符串，表示在连接列表元素时不插入任何字符。如果要插入，直接填在''内，如','。
当列表元素类型不一致时, 需要先将元素类型全部转成string再用join。如: password_hard = ''.join(map(str, password_list))
'''    
print(password_hard)
