n = int(input())
arr = list(map(int, input().split()))
min_val = 100

for i in range(n):
    for j in range(i+1,n):
        if arr[j] - arr[i] < min_val:
            min_val = arr[j] - arr[i]

print(min_val)