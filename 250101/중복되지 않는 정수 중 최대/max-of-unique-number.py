n = int(input())
arr = list(map(int, input().split()))

cnt = [0 for _ in range(n + 1)]

for elem in arr:
    cnt[elem] += 1

ans = -1
for max_val in range(n, -1, -1):
    if cnt[max_val] == 1:
        ans = max_val
        break

print(ans)