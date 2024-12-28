n = input().split()
a, b = int(n[0]), int(n[1])
cnt, sum = 0, 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        cnt += 1

print(sum, f"{sum/cnt:.1f}")