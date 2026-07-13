def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


scores = []

n = int(input("Enter number of players: "))

for i in range(n):
    score = int(input("Enter score: "))
    scores.append(score)
    
bubbleSort(scores)

print("Leaderboard Scores:")

for i in scores:
    print(i, end=" ")