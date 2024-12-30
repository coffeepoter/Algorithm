n = int(input())

for i in range(n):
    for _ in range(i+1):
        print(i+1, end=" ")
    print()