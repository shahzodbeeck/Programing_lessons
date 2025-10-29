# task1
numbers = [10, 20, 30, 40, 50]
numbers[0] = 100
print(numbers)
numbers.append(60)
print(numbers)
print(len(numbers))
# task 2
fruits = ["appl;e", "banana", "cherry"]
fruits[-1:-1] = ['orange', 'kiwi']
print(fruits)
fruits[1] = 'mango'
fruits.sort()
print(fruits)
# task 3
students = ["Ali", "olim", "zarina", "jasur", "sabina"]
print(students.index('zarina'))

# task 4
my_tuple = 5, 10, 15, 20, 25
print(my_tuple[2])
print(len(my_tuple))
# task 5
my_tuple = 1, 2, 3
my_list = [1, 2, 3]
my_list.append(4)
"""we cannot append tuple beacuse is unmutable"""
"""list mutable tuple unmutable ,we need breakets for create list but tuple only need comma"""

# task 6

colors = 'red', 'green', 'blue'
colors = list(colors)
colors.append('yellow')
print(tuple(colors))

# Task 7
numbers = [5, 10, 15, 20, 25]
numbers.append(30)
numbers.reverse()
print(numbers)
my_tuple_2 = 10, 20, 30, 40
my_tuple_2 = list(my_tuple_2)
my_tuple_2.reverse()
print(list(my_tuple_2))
# task 8
num_tuple = (50, 60, 70, 80)
num_list = [10, 20, 30, 40]
num_list.extend(num_tuple)
print("MIn", min(num_list))
print("Max", max(num_list))
# task 9
nested_tuple = (1, 2, (3, 4, 5), 6, 7)
print(nested_tuple[2])
for i in nested_tuple:
    if type(i) == tuple:
        for j in i:
            print(j)
    else:
        print(i)
# task 10
numbers = [2, 4, 6, 8, 10]
new_list = list(map(lambda x: x * 2, numbers))
print(new_list)
# task 11
my_list_2 = ['apple', 'banana', 'cherry', 'date', 'fig']
my_list_2.remove('cherry')
print(my_list_2)
my_list_2.pop(-1)
print(my_list_2)
# task 12
ages = [34, 23, 45, 27, 56, 18]
print(ages.sort())
print(ages.sort(reverse=True))
# task 13
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
numbers = set(numbers)
print(list(numbers))
# task 14
numbers_tup = 10, 50, 25, 5, 100, 75
print(max(numbers_tup))
print(min(numbers_tup))
# task 15
my_list_22 = [10, 20, 30, 40, 50, 60]
list_2 = []
for num in range(0,len(my_list_22) - 1,2):
    list_2.append((my_list_22[num], my_list_22[num + 1]))
print(list_2)
