arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]
sum_val = sum(arr)
len_val = len(arr)
print(sum_val, f"{sum_val/len_val:.1f}")