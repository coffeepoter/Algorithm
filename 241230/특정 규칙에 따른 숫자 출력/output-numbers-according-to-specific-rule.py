n = int(input())
cnt = 1

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print(cnt, end=" ")
        cnt += 1
        if cnt == 10:
            cnt = 1
    print()