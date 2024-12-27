a = input().split()
a1, a2 = int(a[0]), int(a[1])
b = input().split()
b1, b2 = int(b[0]), int(b[1])

if a1 > b1 and a2 > b2:
    print(1)
else:
    print(0)