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