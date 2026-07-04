arr = [20,21,70,80,64,36]
largest = arr[0]
for i in arr:
    if i > largest:
        largest = i
print("The largest number is", largest)
print("The sum of all numbers in the array is", sum(arr))
average = sum(arr)/len(arr)
print("The average of all numbers is",average )