arr = list(map(int, input().split()))
sum_val_1 = 0
sum_val_2, cnt = 0, 0
for i in range(0,10):
    if i % 2 == 1:
        sum_val_1 += arr[i]
    if (i+1) % 3 == 0:
        sum_val_2 += arr[i]
        cnt += 1
avg = sum_val_2 / cnt
print(sum_val_1,f"{avg:.1f}")