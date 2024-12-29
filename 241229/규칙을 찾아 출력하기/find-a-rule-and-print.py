n = int(input())

for i in range(n):
    if i == 0 or i == 5:
        for _ in range(n):
            print("*",end=" ")
        print()
    else:
        for j in range(i):
            print("*", end=" ")
        for k in range(n-i-1):
            print(" ", end=" ")
        print("*")