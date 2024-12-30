n = int(input())
cnt = 1
for i in range(0,n):
    for j in range(0,n):
        if cnt > 9:
            cnt = 1
        print(cnt, end="")
        cnt += 1
    print()