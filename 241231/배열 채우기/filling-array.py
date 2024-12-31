arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

for ele in reversed(arr):
    print(ele, end=" ")
