
#%%List Comprehension                         python专用遍历方法。不仅限于list，还有string, tuple, range

#%%newlist = [new_item for item in number]
#list example
number = [1,2,3]
new_number = [n+1 for n in number]          # n指代item，可替换成任何参数。此处为原list中的每一个item+1.
print(new_number)                           #[2,3,4]

#string example
a = 'apple'
a_litter = [l for l in a]
print(a_litter)                             #output a litter list:['a','p','p','l','e']

#range example
r = range(1,5)                              #range为1，2，3，4
r_list = [n*2 for n in r]                   #output[2,4,6,8].第一个new_sitem如果不做处理就是单纯从range到list

#%% new_list = [new_item for item in number if test] 遍历时筛选，test为筛选条件
name = ['Alex','Caroline','Dave','Eleanar','Freddie']
long_name = [n.upper() for n in name if len(n)>4]   #筛选出长度大于4的名字组成新list，并且新list大写
print(long_name)                            #输出为['CAROLINE', 'ELEANAR', 'FREDDIE']


#%%Dictionary Comprehension
name = ['Alex','Caroline','Dave','Eleanar','Freddie']
#%%new_dict = {new_key:new_value for item in list}
import random
student_score = {student:random.randint(1,100) for student in name}#注意此处变量名，即key：student。
                                #list中的item成为了key（单个值默认为key），所以newkey的变量名和item的变量一致
print(student_score)        #output:{'Alex': 80, 'Caroline': 85, 'Dave': 34, 'Eleanar': 48, 'Freddie': 96}


#%%new_dict = {new_key:new_value for (key,value) in dict.items() if test}

pass_student = {p_student:p_value for (p_student,p_value) in student_score.items() if p_value >= 60}

#前一个部分指的是变化的key和value，后一个部分指的是原来的值。这两个联系中，value和key都没有变更，因此二者一致
#%%Pandas Use
'''
dataframe是需要遍历的那个，iterrows()为方法
for (index,row) in dataframe.iterrows():    此处括号内为随机变量名，因为iterrows是按照index和row两个参数进行迭代的，所以这么写便于维护。
    print(row.somecolumn)                 
    if row.somecolumn == something:
        print(row.anothercolumn)       条件筛选查找
    
'''
#%%{new_key:new_value for (index,row) in df.iterrows()} pandas and dictionary   此为分别将df的index和row化为字典
#定位转化部分全部依赖于开头的new_key和new_value，因此有以下两种标明方式：
#{row.new_key:row.new_value for (index,row) in df.iterrows()}     df中需要转换为key的列:df中需要转化为value的列
#NATO_dict = {r['letter']: r['code'] for (i, r) in df.iterrows()}       如之前所言，写明row和index不必要。

