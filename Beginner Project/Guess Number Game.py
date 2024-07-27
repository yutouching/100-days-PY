#Guess Number Game

import random
from wsgiref.util import guess_scheme
print('Welcome to Guess Number Game!')
#clear()
#用字典储存难度系数
difficulty = {
    'easy'  :10,
    'normal':8,
    'hard'  :5
}
print(f'Guess an integer within 1 to 100. You have three choice of difficulty:')
for level, chance in difficulty.items():                                         #字典遍历方式
    print(f'{level}: You have {chance} chances.')




def game():
    #难度选择
    difficulty_choice = input('Please type your choice: ')
    if difficulty_choice in difficulty:
        chances = difficulty[difficulty_choice]                                 #导出字典难度
    else:
        print("'Invalid Input, defaulting to 'normal'.")
        chances = difficulty['normal']

    right_number = random.randint(1,100)                                        #random生成随机整数方式
    should_continue = True
    while should_continue:
        guess_number = int(input('Please input your guess integer number from 1 too 100: '))
        if 1 <= guess_number <= 100:
            if guess_number > right_number:
                chances -= 1
                print(f'Too high. You still have {chances} chances')
            elif guess_number < right_number:
                chances -= 1
                print(f'Too low. You still have {chances} chances.')
            elif guess_number == right_number:
                print(f'You win! The right number is {right_number}')
                again = input('Would you like to play again[y/n]? :')
                if again == 'y':
                    game()
                else:
                    should_continue = False
        else:
            print('Invalid input, please type integer number from 1 to 100')
            continue
        if chances <=0:
            print(f'Chances have been used up. The right number is {right_number}')
            again = input('Would you like to play again[y/n]? :')
            if again == 'y':
                game()
            else:
                should_continue = False

        


game()

