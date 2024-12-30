n = int(input())
cnt = 2

for i in range(0, n):
    for j in range(0, n):
        if cnt > 8:
            cnt = 2
        print(cnt, end=" ")
        cnt += 2
    print()