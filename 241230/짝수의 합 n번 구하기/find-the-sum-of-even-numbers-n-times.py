n = int(input())

for i in range(n):
    ab = input().split()
    a, b = int(ab[0]), int(ab[1])
    sum = 0
    for j in range(a, b+1):
        if j % 2 == 0:
            sum += j
    print(sum)