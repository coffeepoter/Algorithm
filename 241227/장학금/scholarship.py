n = input().split()
a, b = int(n[0]), int(n[1])

if a >=90 and b >=95:
    print(100000)
elif a>=90 and b >=90:
    print(50000)
else:
    print(0)