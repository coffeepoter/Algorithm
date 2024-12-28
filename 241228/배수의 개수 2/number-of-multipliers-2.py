cnt = 0
num = [int(input()) for _ in range(10)]

for i in range(0,10):
    if num[i] % 2 == 1:
        cnt += 1

print(cnt)