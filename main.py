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
def firstTask():
    emoji = input("Enter an emoji: ")
    n = int(input("Enter a number: "))
    try:

        print(f"{emoji} \n" * n)
    except ValueError:
        print("Please enter a valid number.")


def secondTask():
    regions = ["Andijan", "Samarkand", "Bukhara", "Fergana", "Tashkent"]
    print("Regions:", *regions)


def thirdTask():
    animal = input("Enter an animal: ")
    print(f"The animal you entered is: {animal}")


def fourthTask():
    n = int(input("Enter a number: "))
    try:
        print(n * 2)
    except ValueError:
        print("Please enter a valid number.")


firstTask()
secondTask()
thirdTask()
fourthTask()
