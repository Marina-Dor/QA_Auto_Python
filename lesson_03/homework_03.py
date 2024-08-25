# task 01 == Split the alice_in_wonderland variable so that it spans multiple physical lines

alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."\n'''

# task 02 == Find and display all single quote characters ("'") in text

single_quote_char = alice_in_wonderland.count("'")
print(f"Single quote characters in the text: {single_quote_char}\n")

# task 03 == Print the alice_in_wonderland variable

print(alice_in_wonderland)

"""
    # Tasks 04-10:
    # Translate tasks from the book "Mathematics, 5th grade"
    # to the python language and output the answer, so that it was
    # understandable to a fifth grade child 
"""
# task 04
"""
The area of the Black Sea is 436,402 km2, and the area of the Azov Sea 
is 37,800 km2. What is the area of the Black Sea and the Azov Sea together?
"""
black_sea_area = 436402
azov_sea_area = 37800
seas_total_area = black_sea_area + azov_sea_area
print(f"The total area of Black and Azov seas is {seas_total_area} km2\n")

# task 05
"""
The supermarket chain has 3 warehouses where in total 375,291 goods are placed. 
There are 250,449 goods in the first and second warehouses. On the second and third - 222,950 products.
Find the number of goods placed in each warehouse.
"""
total_amount_of_goods = 375291
goods_in_warehouse_1_and_2 = 250449
goods_in_warehouse_2_and_3 = 222950
goods_in_warehouse_1 = total_amount_of_goods - goods_in_warehouse_2_and_3
goods_in_warehouse_3 = total_amount_of_goods - goods_in_warehouse_1_and_2
goods_in_warehouse_2 = total_amount_of_goods - (goods_in_warehouse_1 + goods_in_warehouse_3)

print(f"""There are {goods_in_warehouse_1} goods in Warehouse 1\n
There are {goods_in_warehouse_2} goods in Warehouse 2\n
There are {goods_in_warehouse_3} goods in Warehouse 3\n""")

# task 06
"""
Mykhailo and his parents decided to buy a computer,
using the "Payment in installments" service.
It is known that it will be necessary to pay 1179 hryvnias/month during the year and a half.
Calculate the cost of the computer.
"""
loan_term = 18
monthly_payment = 1179
computer_cost = loan_term * monthly_payment
print(f"The cost of the computer is {computer_cost} hryvnias\n")

# task 07
"""
Find the remainder from the division of numbers:
a) 8019 : 8 d) 7248 : 6
b) 9907 : 9 e) 7128 : 5
c) 2789 : 5 f) 19224 : 9
"""
numbers_list_1: list[int] = [8019, 9907, 2789, 7248, 7128, 19224]
numbers_list_2: list[int] = [8, 9, 5, 6, 5, 9]

for i in range(len(numbers_list_1)):
    remainder = numbers_list_1[i] % numbers_list_2[i]
    print(f"The remainder from the division of numbers {numbers_list_1[i]} and {numbers_list_2[i]} is {remainder}")
print('\n')

# task 08
"""
Irynka, preparing for her birthday, made a list of
what she needs to order. Calculate how much money she will need
for this order.
Product name    Quantity    Price
Large pizza     4           274 UAH
Medium pizza    2           218 UAH
Juice           4           35 UAH
Cake            1           350 UAH
Water           3           21 UAH
"""
order_list = [
    ["Large pizza", 4, 274],
    ["Medium pizza", 2, 218],
    ["Juice", 4, 35],
    ["Cake", 1, 350],
    ["Water", 3, 21]
]
cost_of_the_order = 0

for item in order_list:
    cost_of_the_order += item[1] * item[2]
print(f"The total cost of the order is {cost_of_the_order} UAH\n")

# task 09
"""
Igor is engaged in photography. He decided to collect all his 232
photos and paste into an album. There is a maximum of 8 photos posted on one page. 
How many pages will be needed for Igor to paste all the photos?
"""
total_number_of_photos = 232
one_page_max_amount_of_photos = 8
pages_needed = int(total_number_of_photos / one_page_max_amount_of_photos)
print(f"Igor will need {pages_needed} pages to paste all the photos\n")

# task 10
"""
The family went on a road trip from Kharkiv to Budapest. 
The distance between these cities is 1600 km. 
It is known that 9 liters of gasoline are needed for every 100 km. 
The capacity of the tank is 48 liters.
1) How many liters of gasoline will be needed for such a trip?
2) How many times, at least, does the family need to go to the tank store on this trip, 
filling up a full tank each time?
"""
distance = 1600
liters_per_100_km = 9
tank_capacity = 48
total_trip_liters_needed = int((distance / 100) * liters_per_100_km)
print(f"The family will need {total_trip_liters_needed} liters of gasoline for a trip from Kharkiv to Budapest\n")
number_of_stops = int(total_trip_liters_needed / tank_capacity)
print(f"The family will need {number_of_stops} times to go to the tank store to fill up a full tank each time")
