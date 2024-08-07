PLACEHOLDER = '[name]'

with open('.\\Input\\Names\\invited_names.txt') as name_file:
    names = name_file.readlines()

with open('.\\Input\\Letters\\starting_letter.txt') as letter_file:
    content = letter_file.read()

for name in names:
    name_ud = name.strip()                 #去除名字文件中因换行产生的多余空格
    new_letter = content.replace(PLACEHOLDER,name_ud)
    with open(f'.\\Output\\ReadyToSend\\letter_for_{name_ud}.docx','w')as completed_letter:
        completed_letter.write(new_letter)


#当前的重点是优化可读性。





#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp