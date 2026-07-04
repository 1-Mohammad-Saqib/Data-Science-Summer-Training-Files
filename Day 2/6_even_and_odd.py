for i in range(1,101):
    print(f"{i} is an odd number" if i % 2 != 0 else f"{i} is an even number")

print(f"The sum of all even numbers from 1 to 100 is:",sum(i for i in range(1,101) if i % 2 == 0))

