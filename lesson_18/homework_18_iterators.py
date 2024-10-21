"""
1. Implement an iterator to output the elements of the list in reverse order.
2. Write an iterator that returns all even numbers in the range 0 to N.
"""
from utils import print_separator


def reverse_order_list(some_list):
    reversed_list = reversed(some_list)
    for value in reversed_list:
        print(value)


class EvenNumbersIterator:
    # Initialising end value and current value
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        else:
            even_number = self.current
            self.current += 2
            return even_number


n = 15
list_of_even_numbers = EvenNumbersIterator(n)

print_separator(100, "-")
print(f"Printing even numbers in range from 0 to {n}:")
print_separator(100, "-")
for number in list_of_even_numbers:
    print(number)


list_to_reverse = [1, 2, 3, "Four", "Five", "Six"]
print_separator(100, "-")
print(f"Printing the list {list_to_reverse} in reversed order:")
print_separator(100, "-")
reverse_order_list(list_to_reverse)
