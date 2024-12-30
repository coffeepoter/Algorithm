n = int(input())
cnt = ord('A')

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print(chr(cnt), end=" ")
        cnt += 1
        if cnt > ord('Z'):
            cnt = ord('A')
    print()