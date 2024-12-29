n = int(input())
cnt = 0
while 1:
    if n >= 1000:
        print(cnt)
        break
    if n % 2 == 0:
        n = 3 * n + 1
    else:
        n= 2 * n + 2
    cnt += 1