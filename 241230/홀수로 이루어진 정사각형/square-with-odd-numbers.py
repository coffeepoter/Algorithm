n = int(input())
k = 11
for i in range(0,n):
    for j in range(0,n):
        print(k + 2 * j, end=" ")
    k += 2
    print()