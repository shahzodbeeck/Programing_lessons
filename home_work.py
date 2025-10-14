def thirdTask():
    shape = input("enter a shape: ")
    n = int(input("enter a number(which shape x contains letters: "))

    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                print(shape, end="")
            else:
                print(" ", end="")
        print()


def fourthTask():
    n = int(input("Enter a number: "))
    symbol = input("Enter a symbol: ")
    for i in range(1, n + 1):
        print(" " * (n - i) + symbol * (2 * i - 1))
    print(" " * (n - 1) + symbol)


def fiveth():
    shape = input("Enter a shape: ")
    n = int(input("Enter a number (height of Z): "))

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n - 1 - i:
                print(shape, end="")
            else:
                print(" ", end="")
        print()


thirdTask()
fourthTask()
fiveth()
