def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input("Enter mark: "))
    marks.append(mark)

bubbleSort(marks)

print("Marks in Ascending Order:")

for i in marks:
    print(i, end=" ")

print()

key = int(input("\nEnter mark to search: "))

result = binarySearch(marks, key)

if result != -1:
    print("Mark Found at Position:", result)
else:
    print("Mark Not Found")
