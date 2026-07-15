a = float(input("Enter a number: "))
b = input("Enter the operator: ")
c = float(input("Enter the second number: "))
if type(b) != str:
    print("Error: Invalid operator.")
elif b == '+':
    print("The sum of a and c is:", a + c)
elif b == '-':
    print("The difference of a and c is:", a - c)
elif b == '*':
    print("The product of a and c is:", a * c)
elif b == '/':
    if c != 0:
        print("The quotient of a and c is:", a / c)
    else:
        print("Error: Division by zero is not allowed.")
elif b == '//':
    if c != 0:
        print("The floor division of a and c is:", a // c)
    else:
        print("Error: Division by zero is not allowed.")
elif b == '%':
    if c != 0:
        print("The modulus of a and c is:", a % c)
    else:
        print("Error: Division by zero is not allowed.")