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


bookIds = []

n = int(input("Enter number of books: "))

for i in range(n):
    book = int(input("Enter Book ID: "))
    bookIds.append(book)

key = int(input("Enter Book ID to search: "))

result = binarySearch(bookIds, key)

if result != -1:
    print("Book Found at Index:", result)
else:
    print("Book Not Found")