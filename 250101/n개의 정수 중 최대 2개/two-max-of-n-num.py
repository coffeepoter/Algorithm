n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[0], arr[1])