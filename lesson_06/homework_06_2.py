# Write a loop that will prompt the user to enter a word that contains the letter "h" (both uppercase and lowercase).
# The loop should not terminate if the user entered a word without the letter "h".


letter_h = "h"
while True:
    word_input = input('Enter a word that contains the letter "h": ')
    if letter_h in word_input.lower():
        print('Yey!!! There is "h" letter')
        break
