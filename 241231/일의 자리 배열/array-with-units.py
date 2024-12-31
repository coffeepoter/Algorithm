arr = list(map(int, input().split()))
for i in range(2, 12):
    arr.append(arr[-1]+arr[-2])
    res = arr[i-2] % 10
    print(res, end=" ")