arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

sum_val = 0
cnt = 0

for ele in arr:
    if ele % 2 == 0:
        sum_val += ele
        cnt += 1

print(cnt, sum_val)