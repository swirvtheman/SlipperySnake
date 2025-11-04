# 1
# store_list = ["milk", "bread", "butter"]
# store_list.append('cheese')
# store_list.insert(0, 'yohgurt')

# print(store_list)
# ------------------------------------------

# 2
# store_list = ['yohgurt', 'milk', 'bread', 'butter', 'cheese']
# store_list.pop()
# store_list.pop(2)

# print(store_list)
# -------------------------------------------

# 3
# list = ["apple", "bananas", "apple", "pear", "apple"]

# print(list.count("apple"))
# print(list.index("apple"))
# --------------------------------------------

# 4
# list = ["apple", "bananas", "apple", "pear", "apple"]
# a = list.copy()
# list.clear()

# print(f"This is the original: {list} and this is the copy of the list: {a}.")
# ---------------------------------------------

# 5
# a)
# fruit = ["apple", "bananas"]
# vegies = ["carrot", "onion"]
# print(f"{fruit + vegies}")

# b)
# fruit = ["apple", "bananas"]
# veggies = ["carrot", "onion"]

# a = veggies.copy()
# b = fruit.copy()

# print(b + a)
# ----------------------------------------------

# 6
# people = ["Zara", "adam", "Bea", "cecilia"]

# sort_up = people.copy()
# sort_up.sort(key=str.casefold)

# sort_down = people.copy()
# sort_down.sort(key=str.casefold, reverse=True)

# print(f"Original: {people}")
# print(f"Ascending: {sort_up}")
# print(f"Descending: {sort_down}")
# -----------------------------------------------

# 7
# supplies = ["penna", "sudd", "block", "parm", "ruler"]

# sort_reverse = supplies.copy()
# sort_reverse.reverse()

# print(f" Reversed: {sort_reverse} and Original: {supplies}")
# -----------------------------------------------

# 8
# numbers = [3, 5, 7, 12, 2, 15, 14, 11, 10, 8, 9, 1, 6, ]
# first_three = numbers.copy()
# print(first_three[0:3])
# print(numbers[-3:])
# print(numbers[0::2])
# ------------------------------------------------

# 9
# animals = ["cat", "dog", "bird", "snake"]
# for number, name in enumerate(animals, start=1):
#    print(f"{number}. {name}")
# -------------------------------------------------

# 10
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# even_numbers = numbers.copy
# even_numbers = tuple(x for x in numbers if x % 2 == 0)
# print(f"Even numbers are: {even_numbers}")
# -------------------------------------------------

# 11
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares_list = [x**2 for x in numbers]
# print(squares_list)
# --------------------------------------------------

# 12
# numbers = list(range(1, 20 + 1))
# even_numbers = numbers.copy()
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
# --------------------------------------------------

# 13
