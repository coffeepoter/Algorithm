n = int(input())
sum, cnt = 0, 0
for _ in range(n):
    sum += int(input())
    cnt += 1

print(sum, f"{sum/cnt:.1f}")