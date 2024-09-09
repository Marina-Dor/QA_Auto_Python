# There is a list with data lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Write code that creates a new list (for example, lst2) that contains only the variable type string contained in lst1.
# The data in the list can be any

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [element for element in lst1 if isinstance(element, str)]
print(lst2)
