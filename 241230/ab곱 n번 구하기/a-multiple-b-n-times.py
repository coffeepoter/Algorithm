n = int(input())
for _ in range(n):
    ab = input().split()
    a, b = int(ab[0]), int(ab[1])
    ans = 1
    for i in range(a,b+1):
        ans *= i
    print(ans)