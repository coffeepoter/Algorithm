a = input().split()
b = input().split()
a1, a2 = int(a[0]), a[1]
b1, b2 = int(b[0]), b[1]

if (a1 >= 19 and a2 == "M") or (b1 >= 19 and b2 == "M"):
    print(1)
else:
    print(0)