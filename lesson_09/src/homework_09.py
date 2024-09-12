def splitting_string_list_to_numbers_and_adding(strings):
    result = []
    for string in strings:
        try:
            # Split the string by comma and convert elements to integers
            numbers = [int(element) for element in string.split(',')]
            # Counting the sum of all numbers
            result.append(numbers)
            total_sum = sum(numbers)
            # Output the sum of all numbers
            print(total_sum)
        except ValueError:
            # If there are non-numeric characters ("qwerty1,2,3" in the example),
            # you need to catch the exception and print "Can't do that!"
            print("I can't do it")
    return result


def the_arithmetic_mean_of_the_list(numbers: list):
    return sum(numbers) / len(numbers)
