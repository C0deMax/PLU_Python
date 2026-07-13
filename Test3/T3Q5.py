bookPrices = []

n = int(input("Enter number of books: "))

for i in range(n):
    price = int(input("Enter book price: "))
    bookPrices.append(price)

newPrice = int(input("Enter new book price: "))

position = len(bookPrices)

for i in range(len(bookPrices)):
    if newPrice < bookPrices[i]:
        position = i
        break

bookPrices.insert(position, newPrice)

print("Updated Book Prices:")

for i in bookPrices:
    print(i, end=" ")
