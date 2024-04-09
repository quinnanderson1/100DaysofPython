# This is where I define all calculation functions to clean up the main program

def addition(num1, num2):
    func_result = num1 + num2
    return float(func_result)


def subtraction(num1, num2):
    difference = num1 - num2
    return float(difference)


def multiplication(num1, num2):
    product = num1 * num2
    return float(product)


def division(num1, num2):
    quotient = num1 / num2
    return float(quotient)


def calculate(first_num, second_num, operation):
    """Performs 4-function calculations"""
    f_operationResult = 0
    operation_name = ""
    if operation == "+":
        operation_name = "adding"
        f_operationResult = addition(first_num, second_num)
    elif operation == "-":
        operation_name = "subtracting"
        f_operationResult = subtraction(first_num, second_num)
    elif operation == "*":
        operation_name = "multiplying"
        f_operationResult = multiplication(first_num, second_num)
    elif operation == "/":
        operation_name = "dividing"
        f_operationResult = division(first_num, second_num)

    print(f"The result of {operation_name} {first_num} and {second_num} is {f_operationResult}.")

    return f_operationResult
