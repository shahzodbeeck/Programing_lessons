def firstTask():
    variable = "I am pdp student"
    print(variable)
    student = "shahzod"
    print(student)
    student = "bobur"
    print(student)
    print(len(variable + student))


def secondTask():
    """
    this task worked as calculator but calculate float and int only +- if yes it does + else it does -
    :return: It is void function
    """
    int_num = int(input("Enter a number: "))
    float_num = float(input("Enter a float number: "))
    while True:
        answer = input("Do you want to add these numbers? (yes/no): ")
        if answer.lower() == "yes":
            print(int_num + float_num)
            break
        elif answer.lower() == "no":
            if int_num > float_num:
                print(int_num - float_num)
                break
            else:
                print(float_num - int_num)
                break
        else:
            print("Invalid input, Please try again.")


firstTask()
secondTask()