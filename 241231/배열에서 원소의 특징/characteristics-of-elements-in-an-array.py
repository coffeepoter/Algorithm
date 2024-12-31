arr = list(map(int, input().split()))

for ele in arr:
    if ele % 3 == 0:
        arr = arr[:arr.index(ele)]
        break
print(arr[-1])