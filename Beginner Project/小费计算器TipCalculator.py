#小费计算器TipCalculator
print('Welcome to Tip Calculator!')
bill = float(input('What was the total bill?\n'))
tip = int(input('How much tips would you like to give? 10%, 12%, or15%?\n'))
split_people = int(input('How many people to split the bill?\n'))

each_bill = round(float((bill*(1+tip/100))/split_people),2)   #四舍五入round，逗号后为要保留的小数，必须统一数字类型为float才能round。
print_bill = str(each_bill)

print('Each person should pay: $' + print_bill)