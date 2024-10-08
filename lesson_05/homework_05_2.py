# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

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
new_person = ('Maryna', 'Doroshenko', 35, 'QA Engineer', 'Dusseldorf')
people_records.insert(0, new_person)
print("-"*100)
print("People records after modifying")
print("-"*100)
print('\n'.join(str(item) for item in people_records))
temp = people_records[1]
people_records[1] = people_records[5]
people_records[5] = temp
print("-"*100)
print("People records after swap")
print("-"*100)
print('\n'.join(str(item) for item in people_records))
print("-" * 100)
print("Condition check result")
print("-" * 100)
for index in [6, 10, 13]:
    if people_records[index][2] >= 30:
        print((
          f"The shortlisted person is or older than 30 years:\n"
          f"{people_records[index]}"
        ))
    else:
        print((
          f"The shortlisted person is younger than 30 years:\n"
          f"{people_records[index]}"
        ))
