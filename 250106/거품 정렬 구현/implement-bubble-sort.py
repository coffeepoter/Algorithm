n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for e in arr:
    print(e, end=" ")