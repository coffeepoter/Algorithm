n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

value = 1
for d in range(n + m - 1):  
    for i in range(max(0, d - m + 1), min(d + 1, n)):
        j = d - i
        if 0 <= j < m:
            arr[i][j] = value
            value += 1

for row in arr:
    print(" ".join(map(str, row)))
