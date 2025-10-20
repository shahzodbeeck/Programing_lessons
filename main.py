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

def homeTask():
    project_name = "Project"
    admin = "admin"
    students = ['Anvar', 'Dilshod', 'Malika']
    print(project_name)
    print(admin)
    print(students)
    students.append("Sardor")
    print("Appendan keyin",students)
    students.insert(1, "Otabek")
    print("Insertdan keyin",students)
    students.extend(['Gulnoza', 'Islom'])
    print("extend keyin",students)
    students.remove("Dilshod")
    print("remove keyin",students)
    print(students.pop(-1))
    print("pop keyin",students)
    del students[0]
    print("del keyin",students)
    students.sort()
    print("sort keyin",students)
    students.sort(reverse=True)
    print("sort reversed keyin",students)
    students.clear()
    print("clear keyin",students)
    print(len(students))
homeTask()