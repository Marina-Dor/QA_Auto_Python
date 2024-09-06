# task 1
""" The task is to print a multiplication table by a given number, but
only up to the maximum value for the product - 25.
The code is almost ready, it is necessary to find errors and correct/complement.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # somewhere there is an error, and maybe more than one
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print("-" * 100)

# task 2
""" Write a function that calculates the sum of two numbers.
"""


def the_sum_of_two_numbers(number1, number2):
    return number1 + number2


result2 = the_sum_of_two_numbers(5, 6)
print("The sum of two numbers is:", result2)
print("-" * 100)

# task 3
""" Write a function that calculates the arithmetic mean of a list of numbers.
"""


def the_arithmetic_mean_of_the_list(numbers: list):
    return sum(numbers) / len(numbers)


result1 = the_arithmetic_mean_of_the_list([4, 5, 6, 9, 10])
print(f"The arithmetic mean of a list of numbers is: {result1}")
print("-"*100)

# task 4
""" Write a function that takes a string and returns it in reverse order.
"""


def reverse_order_string(string: str):
    return string[::-1]


reverse_result = reverse_order_string("H e l l o  W o r l d !")
print(f"The reverse order of the string is: {reverse_result}")
print("-"*100)

# task 5
""" Write a function that takes a list of words and returns the longest word in the list.
"""


def the_longest_word_in_the_list(words: list):
    return max(words, key=len)


longest_word = the_longest_word_in_the_list(["Cucumber", "Potato", "Tomato", "Brocolli", "Cauliflower"])
print(f"The longest word in the list is: {longest_word}")
print("-"*100)

# task 6
""" Write a function that takes two strings and returns the index of the first occurrence of the second string
to the first row if the second row is a substring of the first row, and -1 if the second row
is not a substring of the first line."""


def find_substring(str1, str2):
    return str1.find(str2)


string1 = "Hello, world!"
string2 = "world"
print(find_substring(string1, string2))  # returns 7

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "cat"
print(find_substring(string1, string2))  # returns -1
print("-"*100)

""" Choose any 4 tasks from previous homework and
turn them into 4 functions that get a value and return a result.
Be sure to document functions and give meaningful names to variables.
"""

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# task 7
# Write a function that adds a new record to the beginning of the given list


def add_new_record_to_the_beginning_of_the_list(records: list, new_record: tuple):
    return records.insert(0, new_record)


new_person = ('Maryna', 'Doroshenko', 35, 'QA Engineer', 'Dusseldorf')
add_new_record_to_the_beginning_of_the_list(people_records, new_person)

print("-"*100)
print("People records after modifying")
print("-"*100)
print('\n'.join(str(item) for item in people_records))

# task 8
# In modified list swap elements with indexes 1 and 5 (1<->5). Print result


def swap_elements_indexes(records: list, index1: int, index2: int):
    records[index1], records[index2] = records[index2], records[index1]
    return records


swap_elements_indexes(people_records, 1, 5)
print("-"*100)
print("People records after swap")
print("-"*100)
print('\n'.join(str(item) for item in people_records))

# task 9
# Check that all people in modified list with records indexes 6, 10, 13 have age >=30.


print("-" * 100)
print("Condition check result")
print("-" * 100)


def check_age_at_least_30(records: list, index1: int, index2: int, index3: int):
    for index in [index1, index2, index3]:
        if records[index][2] >= 30:
            print((
                f"The shortlisted person is or older than 30 years:\n"
                f"{records[index]}"
            ))
        else:
            print((
                f"The shortlisted person is younger than 30 years:\n"
                f"{records[index]}"
            ))


check_age_at_least_30(people_records, 6, 10, 13)
print("-" * 100)

# task 10
""" Print how many times the letter "h" occurs in the text
"""
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


def letter_h_counter(text: str, letter: str):
    return text.count(letter)


count_letter_h = letter_h_counter(adventures_of_tom_sawyer, "h")
print(f"\nLetter 'h' occurs in the text {count_letter_h} times")
