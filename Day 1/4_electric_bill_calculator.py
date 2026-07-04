Units = float(input("Enter the electricity units consumed: "))

if Units <= 100:
    total_bill = Units * 5
    print("The total amount of your electricity bill is:", total_bill)
elif Units <= 200:
    total_bill = (100 * 5) + ((Units - 100) * 7)
    print("The total amount of your electricity bill is:", total_bill)
elif Units <= 300:
    total_bill = (100 * 5) + (100 * 7) + ((Units - 200) * 10)
    print("The total amount of your electricity bill is:", total_bill)
elif Units <= 400:
    total_bill = (100 * 5) + (100 * 7) + (100 * 10) + ((Units - 300) * 15)
    print("The total amount of your electricity bill is:", total_bill)
else:
    print("Error: Units consumed is too high.")
    total_bill = None

# if total_bill is not None:
#     print("The total amount of your electricity bill is:", total_bill)