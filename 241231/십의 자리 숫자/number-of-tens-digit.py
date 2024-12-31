arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

for i in range(1, 10):
    cnt = 0
    for elem in arr:
        if (elem // 10) == i:
            cnt += 1
    print(f"{i} - {cnt}")
