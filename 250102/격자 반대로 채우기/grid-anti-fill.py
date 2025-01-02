n = int(input())
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]
num = 1
for j in range(1, n+1):
    if j % 2 == 1:
        for i in range(1,n+1):
            arr[n-i][n-j] = num
            num += 1
    else:
        for i in range(n, 0, -1):
            arr[n-i][n-j] = num
            num += 1

for elem1 in arr:
    for elem2 in elem1:
        print(elem2, end=" ")
    print()