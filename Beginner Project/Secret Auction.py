#Secret Auction
from replit import clear

def highest_biders(bidding_record):
    highest_price = 0                              #定义初始最高价
    winner = ''
    for bidder in bidding_record:                  #for只遍历dictionary中的key
        bid_amount = bidding_record[bidder]         #bid_amount被赋值key下的value。
        if bid_amount > highest_price:
            highest_price = bid_amount             #迭代出最高价
            winner = bidder                         #winner被赋值为key
    print(f'The winner is {winner} with a bid of {highest_price}')

print('Welcome to the secret auction program.\n')
should_continue = True
bids = {}
while should_continue:
    name = input('What is your name?')
    price = int(input('What is your bid? $'))
    bids[name] = price                         #定义key和value
    while True:                                #回答检测专门开一个while循环，结束后另外再做if
        check = input('Are there any other biders? (yes/no)')
        if check in ['yes','no']:
            break
        else:
            print("Incorrect Input! Please type 'yes' or 'no'")
            continue
    
    if check == 'yes':
            clear()
    elif check == 'no':
        should_continue = False
        highest_biders(bids)

