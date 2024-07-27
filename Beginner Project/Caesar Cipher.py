#Caesar Cipher
'''
该程序在VScode上跑不通，但是spyder上可以。
'''
import string

should_continue = True                    #重复使用程序的循环

letter = 2 * list(string.ascii_lowercase) #重复字母的list防止位移溢出
#%% 功能
def caesar(input_text, shift_amount, cipher_direction):
    output = ''
    shift_amount = shift_amount % 26
    if cipher_direction == 'decode':
        shift_amount *= -1  #简便方法。直接变更方向. 在for循环外。
    for l in input_text:
        if l in letter:                 #保留空格和符号
            position = letter.index(l)
            updated_position = position + shift_amount
            output += letter[updated_position]
        else:
            output += l
    return output
  

#%%  课程代码。可以加密/解密信息。
while should_continue:
    direction = input("'encode'or 'decode'?\n").lower()
    if direction not in ['encode', 'decode']:         #输入检测。
        print('Incorrect Input!')
        continue
    else:
        text = input('Type your message:\n').lower()
        shift = int(input('shift number?\n'))
        print(f"Direction: {direction}, Text: {text}, Shift: {shift}")
        caesar(text,shift,direction)

    while True:               #yes or no 的输入错误检测循环
        again = input("Do you want to go again? Type 'yes' or 'no'.\n").lower()
        if again in ['yes', 'no']:
            break
        else:
            print('Incorrect Input!')

    if again == 'no':            #用户终止使用
        should_continue = False
        print('Goodbye!')
    
#%%  不知道方式下的暴力解密代码，循环输出26种可能
def decode_all_shifts(encoded_message):
    for shift in range(26):
        decoded_message = caesar(encoded_message, shift, 'decode')
        print(f'Shift {shift}: {decoded_message}')

encoded_message = input('Type your encrypted message:\n').lower()
decode_all_shifts(encoded_message)



# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for l in plain_text:
#         position = letter.index(l) #字母在letter列表中的位置
#         updated_position = position + shift_amount
#         new_l = letter[updated_position]
#         cipher_text += new_l
#     print(f'The encoded message is: {cipher_text}')

# def decrypt(cipher_text, shift_amount):
#     plain_text = ''
#     for l in cipher_text:
#         position = letter.index(l)
#         back_position = position - shift_amount
#         original_l = letter[back_position]
#         plain_text += original_l
#     print(f'The decoded message is: {plain_text}')

# if 'encode' in direction:
#     encrypt(plain_text=text, shift_amount=shift)
# elif 'decode' in direction:
#     decrypt(cipher_text= text, shift_amount= shift)
# else:
#     print('incorrect input')




