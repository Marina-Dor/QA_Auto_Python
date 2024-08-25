adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# OVERWRITE the contents of the variable adventures_of_tom_sawyer in exercises 1-3
# task 01 ==
""" The data in the row adventures_of_tom_sawyer is broken randomly, due to a bug.
you need to replace the end of the paragraph with a space.replace("\n", " ")"""

adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("\n", " ")

# task 02 ==
""" Replace .... with a space
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.replace("....", " ")

# task 03 ==
""" Correct so that there is no more than one space between words in the text.
"""
adventures_of_tom_sawyer = adventures_of_tom_sawyer.split()
adventures_of_tom_sawyer = " ".join(adventures_of_tom_sawyer)

print(adventures_of_tom_sawyer)

# task 04
""" Print how many times the letter "h" occurs in the text
"""
letter_h_counter = adventures_of_tom_sawyer.count("h")
print(f"\nLetter 'h' occurs in the sentence {letter_h_counter} times")

# task 05
""" Display the number of words in the text that begin with a capital letter?
"""
capitalized_word_counter = 0
for word in adventures_of_tom_sawyer:
    if word.istitle():
        capitalized_word_counter += 1
print(f"\nThere are {capitalized_word_counter} capitalized words in the text")

# task 06
""" Find the position in which the word Tom occurs the second time
"""
tom_finder = adventures_of_tom_sawyer.find("Tom", 3)
print(f"\nThe word Tom occurs for the second time in the {tom_finder} position\n")

# task 07
""" Split the variable adventures_of_tom_sawyer by the end of the sentence.
Store the result in the variable adventures_of_tom_sawyer_sentences
"""
adventures_of_tom_sawyer_sentences = adventures_of_tom_sawyer.split('.')
adventures_of_tom_sawyer_sentences.pop()
print(adventures_of_tom_sawyer_sentences)

# task 08
""" Display the fourth sentence from adventures_of_tom_sawyer_sentences.
Convert the string to lower case.
"""
print(f"\nThe fourth sentence in the text is: {adventures_of_tom_sawyer_sentences[3]}\n")
adventures_of_tom_sawyer_sentences[3] = adventures_of_tom_sawyer_sentences[3].lower()

# task 09
""" Check if any sentence starts with "By the time".
"""
for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.lstrip().capitalize().startswith("By the time"):
        print(sentence)

# task 10
""" Display the number of words in the last sentence of adventures_of_tom_sawyer_sentences. 
"""
words_in_last_sentence = adventures_of_tom_sawyer_sentences[-1].split()
print(f"\nThe number of words in the last sentence is: {len(words_in_last_sentence)}")
