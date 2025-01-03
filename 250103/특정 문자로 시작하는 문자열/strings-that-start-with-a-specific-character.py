n = int(input())
arr = [input() for _ in range(n)]
ch = input()
cnt = 0
sum_val = 0

for elem in arr:
    if elem[0] == ch:
        cnt += 1
        sum_val += len(elem)

print(cnt, f"{sum_val/cnt:.2f}")