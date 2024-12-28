n = input().split()
a, b = int(n[0]), int(n[1])

while a <= b:
    if a % 2 == 0:
        print(a, end=" ")
    a += 1