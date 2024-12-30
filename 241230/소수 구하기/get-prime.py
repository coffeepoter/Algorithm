n = int(input())

for i in range(2,n+1):
    res = True
    for j in range(i-1, 1, -1):
        if i % j == 0:
            res = False
    if res == True:
        print(i, end=" ")