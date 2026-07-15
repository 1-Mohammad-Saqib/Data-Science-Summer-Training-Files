# 4 wap to make a calculator it must work until user wants to exit
# while True:
#     a = float(input("Enter a number: "))
#     b = input("Enter the operator: ")
#     c = float(input("Enter the second number: "))
#     if type(b) != str:
#         print("Error: Invalid operator.")
#     elif b == '+':
#         print("The sum of a and c is:", a + c)
#     elif b == '-':
#         print("The difference of a and c is:", a - c)
#     elif b == '*':
#         print("The product of a and c is:", a * c)
#     elif b == '/':
#         if c != 0:
#             print("The quotient of a and c is:", a / c)
#         else:
#             print("Error: Division by zero is not allowed.")
#     elif b == '//':
#         if c != 0:
#             print("The floor division of a and c is:", a // c)
#         else:
#             print("Error: Division by zero is not allowed.")
#     elif b == '%':
#         if c != 0:
#             print("The modulus of a and c is:", a % c)
#         else:
#             print("Error: Division by zero is not allowed.")

while True:
    print("\n===== Simple Calculator =====")
    print("Enter 'exit' as the operator to quit.")

    a = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, //, %, exit): ").lower()

    if operator == "exit":
        print("Thank you for using the calculator!")
        break

    c = float(input("Enter the second number: "))

    if operator == "+":
        print(f"Result: {a} + {c} = {a + c}")

    elif operator == "-":
        print(f"Result: {a} - {c} = {a - c}")

    elif operator == "*":
        print(f"Result: {a} * {c} = {a * c}")

    elif operator == "/":
        if c != 0:
            print(f"Result: {a} / {c} = {a / c}")
        else:
            print("Error: Division by zero is not allowed.")

    elif operator == "//":
        if c != 0:
            print(f"Result: {a} // {c} = {a // c}")
        else:
            print("Error: Division by zero is not allowed.")

    elif operator == "%":
        if c != 0:
            print(f"Result: {a} % {c} = {a % c}")
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid operator! Please use +, -, *, /, // or %.")

    choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()

    if choice == "no":
        print("Thank you for using the calculator!")
        break