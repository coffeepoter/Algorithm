n = input().split()
a, b = int(n[0]), int(n[1])

if a < b:
    print(1, 0)
else:
    if a == b:
        print(0, 1)
    else:
        print(0, 0)