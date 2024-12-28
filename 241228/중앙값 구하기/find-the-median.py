n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])

if (a < b and a > c) or (a < c and a > b):
    print(a)
elif (b < a and b > c) or (b < c and b > a):
    print(b)
elif (c < a and c > b) or (c < b and c > a):
    print(c)