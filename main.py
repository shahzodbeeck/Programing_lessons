# def firstTask():
#     color = input("Enter a color: ")
#     print(f"Your fovaurete color is {color}")
#     # print("Your fovaurete color is " + color)
#
#
# def secondTask():
#     count_books = int(input("How many books do you want? "))
#     try:4
#         print(f"You have read {count_books} books")
#         # print("You have read " + str(count_books) + " books")
#
#
#     except ValueError:
#         print("Please enter a valid number.")
#
#
# def thirdTask():
#     n = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
#     try:
#         result = n - n2
#         print(
#             f"The result of {n} subtracts  by {n2} is {result}")
#         # print("The result of " + str(n) + " subtracts by " + str(n2) + " is " + str(result))
#
#     except ValueError:
#         print("Please enter valid numbers.")
#
#
# firstTask()
# secondTask()
# thirdTask()
# def firstTask():
#     emoji = input("Enter an emoji: ")
#     n = int(input("Enter a number: "))
#     try:
#
#         print(f"{emoji} \n" * n)
#     except ValueError:
#         print("Please enter a valid number.")
#
#
# def secondTask():
#     regions = ["Andijan", "Samarkand", "Bukhara", "Fergana", "Tashkent"]
#     print("Regions:", *regions)


#
# def thirdTask():
#     animal = input("Enter an animal: ")
#     print(f"The animal you entered is: {animal}")


# def fourthTask():
#     n = int(input("Enter a number: "))
#     try:
#         print(n * 2)
#     except ValueError:
#         print("Please enter a valid number.")

#
# firstTask()
# secondTask()
# thirdTask()
# fourthTask()
# def firstTask():
#     try:
#         n = int(input("Enter a number: "))
#         n1 = int(input("Enter a number: "))
#         print(n % n1)
#         print(n // n1)
#         print(n / n1)
#         print(n + n1)
#         print((n + n1) ** 2)
#     except ValueError:
#         print("Please enter a valid number.")
#
#
# firstTask()
# def secondTask():
#     name = input("Enter your name: ")
#     surname = input("Enter your surname: ")
#     print(f"Your full name is: {name} {surname}")
#
#
# def thirdTask():
#     shape = input("enter a shape: ")
#     n = int(input("enter a number(which shape x contains letters: "))
#
#     for i in range(n):
#         for j in range(n):
#             if j == i or j == n - 1 - i:
#                 print(shape, end="")
#             else:
#                 print(" ", end="")
#         print()

#
#
# def fourthTask():
#     n = int(input("Enter a number: "))
#     symbol = input("Enter a symbol: ")
#     for i in range(1,n+1):
#         print(" "* (n -i)  + symbol * (2 * i - 1))
#     print(" " * (n - 1)+symbol)
#
# def fiveth():
#     shape = input("Enter a shape: ")
#     n = int(input("Enter a number (height of Z): "))
#
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i == n - 1 or j == n - 1 - i:
#                 print(shape, end="")
#             else:
#                 print(" ", end="")
#         print()

# secondTask()
# thirdTask()
# fourthTask()
# fiveth()

# name = "Shahzod"
# print("Hello " + name)
# word = "Python d"
# print(len(word))
# print(word.upper())
# print(word.lower())
# print(word.capitalize())
# print(word.title())
# print(word.isalpha())
# print(word.islower())
# print(word.isnumeric())
# print(word.isupper())
# print(word.isspace())
# print(type(word))


# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*HOMEWORK*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_#
# def firstTask():
#     variable = "I am pdp student"
#     print(variable)
#     student = "shahzod"
#     print(student)
#     student = "bobur"
#     print(student)
#     print(len(variable + student))
#
#
# def secondTask():
#     """
#     this task worked as calculator but calculate float and int only +- if yes it does + else it does -
#     :return: It is void function
#     """
#     int_num = int(input("Enter a number: "))
#     float_num = float(input("Enter a float number: "))
#     while True:
#         answer = input("Do you want to add these numbers? (yes/no): ")
#         if answer.lower() == "yes":
#             print(int_num + float_num)
#             break
#         elif answer.lower() == "no":
#             if int_num > float_num:
#                 print(int_num - float_num)
#                 break
#             else:
#                 print(float_num - int_num)
#                 break
#         else:
#             print("Invalid input, Please try again.")
#
#
# firstTask()
# secondTask()
# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*| Lesson Tasks |*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_#
# del element uchiradi without returning
# pop elementni index bilan uchiradi returin qiladi
# remove elementni uzini value bilan uchiradi
# insert qushadi indexga
# append ohiriga qushadi
# del indexsiz bersa listni full uchiradi o'zgaruvchini ham
# clear listni tozalidi []
# extend 2 ta listni qoshadi alternative +
# sort saralaydi
# ascending -1-9 descending 9-0
# len lengini qaytaradu startdan endgachon oladi end'ni o'zi kirmaydi -1 ohirgisini oladi
# vegetables = ["carrot", "potato", "tomato", "onion"]
# print(vegetables[2])
# my_list = [1, 2, 3, 4, 5]
# print(my_list[0])
# print(my_list[4])
# my_list_2 = [1, 2, 3, 4, 5]
# my_list_2.append(6)
# print(my_list_2)
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1, "banana")
# print(fruits)
# def fisrtTask():
#     fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
#     fruits.pop(1)
#     fruits.pop(2)
#     print(fruits)
#
#
# fisrtTask()
#
#
# def secondTask():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     oddnumbers = list(filter(lambda x: x % 2 != 0, numbers))
#     print(oddnumbers)
#
#
# secondTask()
#
#
# def thirdTask():
#     my_list = [10, 20, 30, 40, 50, 60, 70, 80]
#     del my_list[3:5]
#     print(my_list)
#
#
# thirdTask()
#
#
# def fourthTask():
#     cities = ["New york", "london", "TOkyo", "Moscow", "Paris"]
#     cities.pop(2)
#     print(cities)
#
#
# fourthTask()


# def fifthTask():
#     numbers = [5, 10, 15, 20, 25]
#     numbers.pop(0)
#     numbers.pop(-1)
#     print(numbers)
#
#
# fifthTask()
#
#
# def sixthTask():
#     fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
#     fruits = [fruits.pop(1)]
#     print(fruits)
#
#
# sixthTask()
#
#
# def seventhTask():
#     items = [1, 2, 3, 4, 5]
#     items.clear()
#     print(items)
#
#
# seventhTask()
#
#
# def eighthTask():
#     cars = ['Toyota', 'Ford', 'BMW', "Audi"]
#     cars.append(cars.pop(1))
#     print(cars)
#
#
# eighthTask()
#
#
# def ninthTask():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     numbers.reverse()
#     print(numbers)
#
#
# ninthTask()

# def homeTask():
#     project_name = "Project"
#     admin = "admin"
#     students = ['Anvar', 'Dilshod', 'Malika']
#     print(project_name)
#     print(admin)
#     print(students)
#     students.append("Sardor")
#     print("Appendan keyin",students)
#     students.insert(1, "Otabek")
#     print("Insertdan keyin",students)
#     students.extend(['Gulnoza', 'Islom'])
#     print("extend keyin",students)
#     students.remove("Dilshod")
#     print("remove keyin",students)
#     print(students.pop(-1))
#     print("pop keyin",students)
#     del students[0]
#     print("del keyin",students)
#     students.sort()
#     print("sort keyin",students)
#     students.sort(reverse=True)
#     print("sort reversed keyin",students)
#     students.clear()
#     print("clear keyin",students)
#     print(len(students))
# homeTask()

# _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*| Lesson Tasks (Tuple)|*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_#

# numbers =(1,2,3,4,5)
# print(numbers)
# print(type(numbers))
# single_tupleee

# single_tuple =(1,)
# print(single_tuple)
# print(type(single_tuple))
# nums =(1,2,3,4,5)
# nums[0] =4
# print(nums)

# computer_elements =('Cpu','Keyboard','Motherboard','Keyboard','Keyboard')
# print(computer_elements.index('Cpu'))
# print(computer_elements.count('Keyboard'))

# fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi')
# print(fruits[0])
# print(fruits[-1])
# print(fruits.index('cherry'),fruits[fruits.index('cherry')])
#
# numbers =(1,2,3,4,2,5,6,2)
# print(numbers.count(2))
# print(numbers.index(5))
#
# colors = ('red', 'green', 'blue')
# colors =list(colors)
# colors.append('yellow')
# print(tuple(colors))
#
# letters = ('a', 'b', 'c', 'd', 'e')
# letters = list(letters)
# letters.reverse()
# print(tuple(letters))
#
# nested = (1,2,(3,4,5),6,7)
# print(nested[2])
# for item in nested:
#     if type(item) == tuple:
#         for i in item:
#             print(i)
#     else:
#         print(item)

# my_tuple =(10,20,30,40,50)
# my_tuple = list(my_tuple)
# my_tuple.append(60)
# print(tuple(my_tuple))
#
# first_tuple =(1,2,3,4)
# second_tuple = (5,6,7,8)
# third_tuple = first_tuple + second_tuple
# print(third_tuple)
# #-----------------------Task 1 -------------------#
#
# my_tup =4,6,2,8,3,1
# print(my_tup)
# my_tup=list(my_tup)
# my_tup.append(9)
# print(tuple(my_tup))
# list(my_tup)
# my_tup[4:4]=[15,20,25]
# print(list(my_tup))
# my_tup.append(30)
# print(tuple(my_tup))
#
# #-------------------------------------Task 2---------------------------------#
# print("Task 2")
# tup_2=10,4,7,2,9,1,5
# tup_2=list(tup_2)
# tup_2.append(12)
# print(tuple(tup_2))
# tup_2=list(tup_2)
# tup_2[2:2]=[20,25]
# print(tuple(tup_2))
# tup_2=list(tup_2)
# tup_2.remove(min(tup_2))
# tup_2.sort()
# tup_2.insert(0,100)
# print(tuple(tup_2))

# # task1
# numbers = [10, 20, 30, 40, 50]
# numbers[0] = 100
# print(numbers)
# numbers.append(60)
# print(numbers)
# print(len(numbers))
# # task 2
# fruits = ["appl;e", "banana", "cherry"]
# fruits[-1:-1] = ['orange', 'kiwi']
# print(fruits)
# fruits[1] = 'mango'
# fruits.sort()
# print(fruits)
# # task 3
# students = ["Ali", "olim", "zarina", "jasur", "sabina"]
# print(students.index('zarina'))
#
# # task 4
# my_tuple = 5, 10, 15, 20, 25
# print(my_tuple[2])
# print(len(my_tuple))
# # task 5
# my_tuple = 1, 2, 3
# my_list = [1, 2, 3]
# my_list.append(4)
# """we cannot append tuple beacuse is unmutable"""
# """list mutable tuple unmutable ,we need breakets for create list but tuple only need comma"""
#
# # task 6
#
# colors = 'red', 'green', 'blue'
# colors = list(colors)
# colors.append('yellow')
# print(tuple(colors))
#
# # Task 7
# numbers = [5, 10, 15, 20, 25]
# numbers.append(30)
# numbers.reverse()
# print(numbers)
# my_tuple_2 = 10, 20, 30, 40
# my_tuple_2 = list(my_tuple_2)
# my_tuple_2.reverse()
# print(list(my_tuple_2))
# # task 8
# num_tuple = (50, 60, 70, 80)
# num_list = [10, 20, 30, 40]
# num_list.extend(num_tuple)
# print("MIn", min(num_list))
# print("Max", max(num_list))
# # task 9
# nested_tuple = (1, 2, (3, 4, 5), 6, 7)
# print(nested_tuple[2])
# for i in nested_tuple:
#     if type(i) == tuple:
#         for j in i:
#             print(j)
#     else:
#         print(i)
# # task 10
# numbers = [2, 4, 6, 8, 10]
# new_list = list(map(lambda x: x * 2, numbers))
# print(new_list)
# # task 11
# my_list_2 = ['apple', 'banana', 'cherry', 'date', 'fig']
# my_list_2.remove('cherry')
# print(my_list_2)
# my_list_2.pop(-1)
# print(my_list_2)
# # task 12
# ages = [34, 23, 45, 27, 56, 18]
# print(ages.sort())
# print(ages.sort(reverse=True))
# # task 13
# numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# numbers = set(numbers)
# print(list(numbers))
# # task 14
# numbers_tup = 10, 50, 25, 5, 100, 75
# print(max(numbers_tup))
# print(min(numbers_tup))
# # task 15
# my_list_22 = [10, 20, 30, 40, 50, 60]
# list_2 = []
# for num in range(len(my_list_22) - 1):
#     list_2.append((my_list_22[num], my_list_22[num + 1]))
# print(list_2)
#task 16
alphabet =('a','b','c','d','e','f','g')
new_tup =alphabet[0:3]
print(new_tup)
lasts = alphabet[-3:]
print(lasts)

#tasks 17
names = ['Ali','Olim','Zarina','Jasur']
for i in names:
    print(i + " - talaba")
#tasks 18
temperatures = 22,25,28,30,27,23
for i in temperatures:
    print(str(i) + " Temperatures")
#task 19
my_list=[1,5,'banana',10,'apple',20]
sum_values = filter(lambda x: type(x) == int, my_list)
print(sum(list(sum_values)))
#task 20
my_list =[10,20,30]
my_tup = 40,50,60
my_tup =list(my_tup)
my_list[0],my_tup[0]=my_tup[0],my_list[0]
print(my_list)
print(tuple(my_tup))