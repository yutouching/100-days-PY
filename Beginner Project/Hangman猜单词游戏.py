from replit import clear


import random

stage = ['0%', '20%', '40%', '60%', '80%', '100%']
lives = 6

# 1. Generate a random word
word_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
choice_word = random.choice(word_list)

# 2. Generate as many blanks as letters in word
char_list = list(choice_word)  # 单词的字母列表
word_length = len(choice_word)
display = ['_' for _ in range(word_length)]  # 对应数量的空白列表

# 3. Ask user to input their guess letter
end_of_game = False

while not end_of_game:
    guess = input('Guess a letter: ').lower()

    clear() #每次作出猜测后清除屏幕内容。游戏体验。

    # 4. Check whether the guessed letter is in the word
    if guess in char_list:
        for position in range(word_length):
            if char_list[position] == guess:
                display[position] = guess
        print(' '.join(display))
        
        if '_' not in display:
            end_of_game = True
            print('You Win! The word was:', choice_word)
    else:
        lives -= 1
        print('Wrong guess.')
        print(stage[lives])
        
        if lives == 0:
            end_of_game = True
            print('You Lose. The word was:', choice_word)




