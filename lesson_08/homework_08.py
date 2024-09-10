# Create an array with strings that will consist of comma-separated numbers.
#
# Use the try\except block to escape characters other than numbers in the list.
#
# For this example, the correct output will be 10, 60, “I can't do it”

string_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# For each element of the list,  (create a new function for this).


def splitting_string_list_to_numbers_and_adding(strings):
    for string in strings:
        try:
            # Split the string by comma and convert elements to integers
            numbers = [int(element) for element in string.split(',')]
            # Counting the sum of all numbers
            total_sum = sum(numbers)
            # Output the sum of all numbers
            print(total_sum)
        except ValueError:
            # If there are non-numeric characters ("qwerty1,2,3" in the example),
            # you need to catch the exception and print "Can't do that!"
            print("I can't do it")


splitting_string_list_to_numbers_and_adding(string_array)
