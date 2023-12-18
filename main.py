
def returnAdd(num1,num2):
    return num1 + num2
def returnSub(num1,num2):
    return num1 - num2
def returnMul(num1,num2):
    return num1 * num2
def returnDiv(num1,num2):
    return num1 / num2
def returnPow(num1,num2):
    return num1 ** num2


def calc(num1, num2, operator):
    res = 0
    flag = 0
    if num1.isnumeric() and num2.isnumeric() and (operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^"):
        flag = 1
        if operator == "+":
            res = returnAdd(int(num1), int(num2))
        elif operator == "-":
            res = returnSub(int(num1), int(num2))
        elif operator == "*":
            res = returnMul(int(num1), int(num2))
        elif operator == "/":
            res = returnDiv(int(num1), int(num2))
        elif operator == "^":
            res = returnPow(int(num1), int(num2))
    return flag, res

def calcInterface():
    cont = "1"
    print("Calculator ")
    print("____________")
    print(" choose operation : \n + = addition \n - = subtraction \n * = multiplication \n / = divination \n ** = power \n ")
    print("____________________________________________")
    num1, num2 = 0,0
    operand = ""
    flag1, res1 = 0, 0
    while cont == "1":
        num1 = input(" enter the first number : ")
        operand = input(" enter the operand : ")
        num2 = input(" enter the second number : ")
        flag1, res1 = calc(num1, num2, operand)
        while flag1 == 0:
            print("invalid operation, please retry")
            num1 = input(" enter the first number : ")
            operand = input(" enter the operand : ")
            num2 = input(" enter the second number : ")
            flag1, res1 = calc(num1, num2, operand)

        print(str(num1) + operand + str(num2) + " = " + str(res1))
        cont = input("would you like to continue ? enter 0 for no, 1 for yes.")
        while cont != "0" and cont != "1":
            cont = input("invalid value. \nwould you like to continue ? enter 0 for no, 1 for yes. ")

    return

def main():
    calcInterface()

if __name__ == "__main__":
    main()