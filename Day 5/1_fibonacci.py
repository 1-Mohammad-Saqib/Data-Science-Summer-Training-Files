# 1 wap to find fibonacci series up to n terms
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print(a, b, end=" ")
for _ in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c