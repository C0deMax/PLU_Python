def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


rollNumbers = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    rollNumbers.append(roll)

key = int(input("Enter roll number to search: "))

result = linearSearch(rollNumbers, key)

if result != -1:
    print("Student Found at Position:", result)
else:
    print("Student Not Found")