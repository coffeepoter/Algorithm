arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

for ele in arr:
    if ele >= 250:
        break
    sum_val += ele
    cnt += 1 

print(f"{sum_val} {sum_val/cnt:.1f}")    