#Calculator（加减乘除连续计算版，无括号）
#未检测number的invalid输入。

def add(n1, n2):
  return n1 + n2    #比起print， return的优势在于可以直接调用

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():         #定义函数用于调用自己（递归）
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ") 
        num2 = float(input("What's the next number?: "))
        calculation_function = operations.get(operation_symbol)#operations[operation_symbol]如果operations_symbol在字典中不存在，会引发KeyError。
        #operations.get(operation_symbol)，会返回None或提供的默认值operations.get(operation_symbol, default_value)。所以如果test用后者。
        if calculation_function:                      #calculation_function 是否为真。检测用户输入的运算符号是否有效。
            answer = calculation_function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            check_repeat = input(f'Do you want to continue calculating with {answer}, or start a new calculation?[y/n]')

            if check_repeat.lower() == 'n':
                should_continue = False
                calculator()                                    #这里递归，开始了一个全新的计算          
            elif check_repeat.lower() == 'y':
                num1 = answer
            else:
                print("Invalid input, please enter 'y' or 'n'.")
        else:
           print("Invalid Input. Please enter '+', '-', '*', '/'.")

calculator()