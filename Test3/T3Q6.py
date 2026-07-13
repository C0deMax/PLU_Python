def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


branch1 = [] 
branch2 = []

n1 = int(input("Enter number of employees in Branch 1: "))

for i in range(n1):
    salary = int(input("Enter salary: "))
    branch1.append(salary)

n2 = int(input("Enter number of employees in Branch 2: "))

for i in range(n2):
    salary = int(input("Enter salary: "))
    branch2.append(salary)

allSalaries = branch1 + branch2

bubbleSort(allSalaries)

print("Employee Salaries in Ascending Order:")

for i in allSalaries:
    print(i, end=" ")

                       

