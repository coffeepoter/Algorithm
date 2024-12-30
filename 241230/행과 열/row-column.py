n = input().split()
a, b = int(n[0]), int(n[1])

for i in range(1, a+1):
    for j in range(1,b+1):
        print(i*j, end=" ")
    print()