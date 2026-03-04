'''

num1=input("Enter the number: ")
num2=input("Enter the number: ")
operators=("Enter the operators(+,-,*,/,**): ")
if operator == '+':
    print("Result: ",num1+num2)
elif operator == '-':
    print("Result: ",num1-num2)
elif operator == '*':
    print("Result: ",num1*num2)
elif 


'''







# Calculator without choice/menu

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operator")
