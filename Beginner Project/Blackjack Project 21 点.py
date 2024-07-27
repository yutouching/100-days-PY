# Blackjack Project 21 点
# %% package
# from replit import clear
import random

# %% variables
# 卡牌总数list。目前只有一副牌
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
# 用户和电脑初始卡牌的列表
user_cards = []
computer_cards = []

# %% function
# 定义Ace规则
def Ace(current_total):
    if current_total + 11 > 21:
        return 1
    else:
        return 11

# 特殊值：A和JQK的计算
def get_value(card, current_total):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return Ace(current_total)
    else:
        return card

# 随机抽卡
def draw_card():
    return random.choice(cards)

# 初始卡牌
def initial_cards():
    global user_cards, computer_cards          #将全局变量global variable的value引入到方程的局部变量local variable中
    user_cards = [draw_card(), draw_card()]
    computer_cards = [draw_card(), draw_card()]

# 总的卡牌值计算
def calculate_total(cards):
    total = 0
    aces = 0
    for card in cards:
        if card == 'A':
            aces += 1  # 计算A的数量
        else:
            total += get_value(card, total)

    # 处理 Ace 的值
    for _ in range(aces):
        total += Ace(total)
    return total

# 判断有没有bust（超过21）
def settlement():
    global user_bust, user_total, computer_total
    user_total = calculate_total(user_cards)
    computer_total = calculate_total(computer_cards)
    print(f'Your cards: {user_cards}, total: {user_total}')
    print(f'Computers cards: {computer_cards}, total: {computer_total}')
    
    if user_total > 21:
        user_bust = True
        print('You went over 21 and busted!')

def judgement():
    user_total = calculate_total(user_cards)
    computer_total = calculate_total(computer_cards)
    if user_total > 21 or (user_total < computer_total <= 21):
        print('You Lose :-(')
    elif user_total == computer_total:
        print('A Tie')
    else:
        print('You Win! ;-)')

# %% Run the game
def game():
    print('Welcome to Blackjack!')
    should_continue = True
    global user_cards, computer_cards, user_bust
    while should_continue:
        # clear()
        start = input('Do you want to start the game? [y/n]: ')
        if start == 'y':
            initial_cards()
            user_bust = False
            print(f'Your cards: {user_cards}, computer\'s cards: {computer_cards}')
            
            while not user_bust:
                settle = input('Do you want to draw another card? [y/n]: ')
                if settle == 'y':
                    user_cards.append(draw_card())
                    settlement()
                    if user_bust:
                        break
                else:
                    break

            while calculate_total(computer_cards) < 17:
                computer_cards.append(draw_card())
                computer_total = calculate_total(computer_cards)
                print(f'Computers cards: {computer_cards}, total: {computer_total}')
                
            judgement()

            again = input('Do you want to restart the game? [y/n]: ')
            if again == 'y':
                user_cards = []
                computer_cards = []
            else:
                should_continue = False
        elif start == 'n':
            should_continue = False

game()













