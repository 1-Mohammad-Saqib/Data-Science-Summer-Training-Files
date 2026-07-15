# 80 + a
# 79 to 60 b
# 59 to 50 c
# else fail

# Grade = int(input("Enter the marks: "))
# if Grade >= 80:
#     print("The grade is A")
# elif Grade >= 60 and Grade < 80:
#     print("The grade is B")
# elif Grade >= 50 and Grade < 60:
#     print("The grad is c")
# elif Grade > 100 or Grade < 0:
#     print("Invalid marks")
# else:
#     print("You are fail")

Grade = int(input("Enter the marks: "))
for i in range (80,101):
    if i == Grade:
        print("The grade is A")
for i in range (60,80):
    if i == Grade:
        print("The grade is B")