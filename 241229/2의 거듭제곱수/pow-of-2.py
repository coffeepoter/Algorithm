n = int(input())
cnt = 0
while 1:
    if n != 1:
        n = n // 2
        cnt += 1
    else:
        break
print(cnt)