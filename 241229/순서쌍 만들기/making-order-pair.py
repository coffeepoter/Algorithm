n = int(input())

for i in range(n):
    for j in range(n):
        print("(", end="")
        print(n-i, end="")
        print(",", end="")
        print(n-j, end="")
        print(")", end="")
        print(" ", end="")
    print()