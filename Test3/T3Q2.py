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


productIds = []

n = int(input("Enter number of products: "))

for i in range(n):
    product = int(input("Enter product ID: "))
    productIds.append(product)

key = int(input("Enter product ID to search: "))

result = binarySearch(productIds, key)

if result != -1:
    print("Product Found at Index:", result)
else:
    print("Product Not Available")