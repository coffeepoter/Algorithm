n = int(input())
arr = list(map(int, input().split()))

while 1:
    max_val = max(arr)
    idx = arr.index(max_val)

    print(idx+1, end=" ")

    if idx == 0:
        break

    arr = arr[:idx]