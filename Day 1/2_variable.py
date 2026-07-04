# Benefits of variables in python
# 1. Variables reduce the need to repeat long values


print('''Rules of variable naming in python:\n1. Variable name can only start with a letter or an underscore\n2. Variable name can only contain letters, numbers, and underscores\n3. Variable name cannot be a reserved keyword in python\n4. Variable name cannot contain spaces\n5. Variable name cannot start with a number\n6. Variable name cannot contain special characters\n7. Variable name cannot be a single character\n8. Variable name cannot be a single underscore\n9. Variables are case sensitive\n''' )

a = 10
b = 21
print("These are arithmetic operators:", "\nThe sum of a and b is:", a + b, "\nThe difference of a and b is:", a - b, "\nThe product of a and b is:", a * b, "\nThe division of a and b is:", a / b, "\nThe floor division of a and b is:", a // b, "\nThe modulus of a and b is:", a % b, "\nThe power of a and b is:", a ** b)

print("These are comparison operators:", "\nThe value of a is equal to b is:", a == b, "\nThe value of a is not equal to b is:", a != b, "\nThe value of a is greater than b is:", a > b, "\nThe value of a is less than b is:", a < b, "\nThe value of a is greater than or equal to b is:", a >= b, "\nThe value of a is less than or equal to b is:", a <= b)

name = "BBD"
age = 25
price = 99.9
print(f"The name is {name}, The price is {price}, and age is {age}")
print("The type of name is ", type(name))
print("The type of age is ", type(age))
print("The type of price is ", type(price))

entered_name = input("Enter the name: ")
print(f"The entered name is {entered_name}")
print("The type of the entered name is ", type(entered_name))

c = float(input("Enter the temperature in Celsius: "))
f = (c * 9/5)+ 32
print("The temperature in Fahrenheit is:", f)