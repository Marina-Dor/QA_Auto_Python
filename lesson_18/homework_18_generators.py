
from utils import print_separator
"""
1. Write a generator that returns a sequence of even numbers from 0 to N.
2. Create a generator that generates a Fibonacci sequence up to a certain number N.
"""


def generate_even_numbers_from_zero_to_n(n):
    # Iteration within the range of numbers from 0 to n with the step 2
    # n + 1 because n value is out of the range
    for number in range(0, n + 1, 2):
        yield number


def generate_fibonacci_sequence_up_to_n(n):
    # Starting numbers
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


n = 17

generator = generate_even_numbers_from_zero_to_n(n)
print_separator(100, "-")
print(f"Printing even numbers in range from 0 up to {n}:")
print_separator(100, "-")
for value in generator:
    print(value)

print_separator(100, "-")
print(f"Printing Fibonacci sequence from 0 up to {n}:")
print_separator(100, "-")
for number in generate_fibonacci_sequence_up_to_n(n):
    print(number)
