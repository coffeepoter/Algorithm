n = input().split()
a, b = int(n[0]), int(n[1])

if a>0:
    for _ in range(b):
        print(a, end="")
else:
    print(0)