def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


priority = []

n = int(input("Enter number of patients: "))

for i in range(n):
    p = int(input("Enter patient priority: "))
    priority.append(p)

bubbleSort(priority)

print("Patients Priority Order:")

for i in priority:
    print(i, end=" ")