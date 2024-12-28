n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)