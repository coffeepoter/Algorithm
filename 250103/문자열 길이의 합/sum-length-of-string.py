n = int(input())
arr = [input() for _ in range(n)]
sum_val = 0
cnt = 0
for elem in arr:
    sum_val += len(elem)
    if elem[0] == "a":
        cnt += 1

print(sum_val, cnt)