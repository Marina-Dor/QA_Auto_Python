# Count the number of unique characters in a line.
# If there are more than 10 - display True in the console, otherwise - False.
# Get the string using the input() function

input_holder = input('Enter something: ')
char_counter = {}
for char in input_holder:
    if char in char_counter:
        char_counter[char] += 1
    else:
        char_counter[char] = 1
# print(f'''You entered "{input_holder}" it consists of {char_counter} characters''')

unique_char_counter = 0
for char, number in char_counter.items():
    if number == 1:
        unique_char_counter +=1

if unique_char_counter > 10:
    print(True)
else:
    print(False)
