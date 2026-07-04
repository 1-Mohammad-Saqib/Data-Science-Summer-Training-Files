# 3 wap to calculate the gross income of a family of 4 members with gst
income = []
for i in range(4):
    salary = float(input(f"Enter the salary of member {i+1}: "))
    income.append(salary)
gross_income = sum(income)
gst = gross_income * 0.18  # Assuming 18% GST
total_income = gross_income + gst
print(f"The gross income of the family is: {gross_income}")
print(f"The GST amount is: {gst}")
print(f"The total income of the family is: {total_income}")
