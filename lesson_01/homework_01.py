# task 01 == Fix syntax errors
print("Hello", end=" ")
print("world!")

# task 02 == Fix syntax errors
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Insert the missing variable into the function print
for letter in "Hello world!":
    print(letter)

# task 04 == Make it so that the number of bananas is
# is always four times larger than apples
apples = 2
banana = apples * 4

# task 05 == Fix variables names
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Calculate the perimeter of the figure from task 05
# and print it to the user
perimeter = side_1 + side_2 + side_3 + side_4
print(perimeter)


"""
    # Tasks 07-10:
    # Translate tasks from the book "Mathematics, 2nd grade"
    # to the python language and print the answer, so that it was
    # understandable to a second grade child 
"""
# task 07
"""
4 apple trees were planted in the garden. Pears are 5 more than apple trees, and plums are 2 less.
How many trees were planted in the garden?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
trees_in_garden = apple_tree + pear_tree + plum_tree
#print(str(trees_in_garden) + " trees were planted in the garden")
print(f"{trees_in_garden} trees were planted in the garden")
# task 08
"""
By noon, the air temperature was 5 degrees above zero.
After lunch, the temperature dropped by 10 degrees.
In the evening it warmed by 4 degrees. What is the temperature at night?
"""
temp_0 = 0
temp_before_lunch = temp_0 + 5
temp_after_lunch = temp_before_lunch - 10
temp_evening = temp_after_lunch + 4
#print("The temperature in the evening is " + str(temp_evening) + " degree")
print(f"The temperature in the evening is {temp_evening} degree")
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
theater_group_boys = 24
theater_group_girls = theater_group_boys / 2
theater_group_kids_today = int((theater_group_boys - 1) + (theater_group_girls - 2))
# print("There are " + str(theater_group_kids_today) + " kids in the group today")
print(f"There are {theater_group_kids_today} kids in the group today")

# task 10
"""
The first book costs 8 hryvnias, the second - 2 hryvnias more expensive,
and the third - as half the cost of the first and second together.
How much will all the books cost if you buy one copy each?
"""
first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) / 2
total_cost = int(first_book + second_book + third_book)
# print("The total cost of the books is: " + str(total_cost) + " hrn")
print(f"The total cost of the books is: {total_cost} hrn")
