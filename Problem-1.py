#input from the user (+, -, *, or /)
operator = input("enter an operator(+ - * /):")

#input and convert it to a floating-point value
num1 = float(input("enter the 1st num:"))
num2 = float(input("enter the 2st num:"))

#Check if the operator is add sub mul & div
if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1 * num2
    print(result)

elif operator == "/":
    result = num1 / num2
    print(result)
    
# If the operator is not one of the above, it is invalid
else:
    print(f"{operator} is not valid")

