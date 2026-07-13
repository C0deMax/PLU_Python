def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


timings = []

n = int(input("Enter number of participants: "))

for i in range(n):
    time = float(input("Enter timing: "))
    timings.append(time)

bubbleSort(timings)

print("Race Timings (Fastest to Slowest):")

for i in timings: 
    print(i, end=" ")