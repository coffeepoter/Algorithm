n = int(input())
cnt = 9
for i in range(0, n):
    for i in range(0, n):
        print(cnt, end="")
        cnt -= 1
        if cnt == 0:
            cnt = 9
    print()