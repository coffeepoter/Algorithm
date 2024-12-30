n = input().split()
start, end = int(n[0]), int(n[1])
cnt = 0

for i in range(start, end+1):
    sum = 0
    for j in range(i-1,0,-1):
        if i % j == 0:
            sum += j
    if sum == i:
        cnt +=1
print(cnt)