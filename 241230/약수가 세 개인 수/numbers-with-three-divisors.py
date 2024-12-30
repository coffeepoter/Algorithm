n = input().split()
start, end = int(n[0]), int(n[1])
res = 0

for i in range(start, end+1):
    cnt = 0
    for j in range(i,0,-1):
        if i % j == 0:
            cnt += 1
    if cnt == 3:
        res += 1
print(res)