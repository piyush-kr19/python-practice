# Python Calculator

operator = input("Enter an operator (+ - * /): ")

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if operator == '+':
    answer = n1 + n2
    print(round(answer))
elif operator == '-':
    answer = n1 - n2
    print(round(answer))
elif operator == '*':
    answer = n1 *n2
    print(round(answer))
elif operator == '/':
    answer = n1 / n2
    print(round(answer))
else:
    print("Invalid Operator")
    