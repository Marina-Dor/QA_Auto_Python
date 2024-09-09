# There is a list of numbers, count the sum of all EVEN numbers in this list

numbers = [1, 5, 6, 8, 220, 951, 102, 95, 17, 18, 50]
sum_of_even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        sum_of_even_numbers += number
print(f"The sum of all EVEN numbers in the list is {sum_of_even_numbers}")
