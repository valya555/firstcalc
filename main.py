
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


def calc(num1,num2, operator):
    res = 0
    flag = 0
    if num1.isdigit and num2.isdigit and (operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^"):
        flag = 1
        if operator == "+":
            res = returnAdd(num1, num2)
        elif operator == "-":
            res = returnSub(num1, num2)
        elif operator == "*":
            res = returnMul(num1, num2)
        elif operator == "/":
            res = returnDiv(num1, num2)
        elif operator == "+":
            res = returnAdd(num1, num2)
    return flag, res