#2 wap to to evaluate a string whether it is palindrome or not
s = input("Enter a string: ")
s = s.replace(" ", "").lower()
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")