n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])

if a == min(a,b,c):
    print(1, end=" ")
else:
    print(0, end=" ")

if a==b==c:
    print(1)
else:
    print(0)