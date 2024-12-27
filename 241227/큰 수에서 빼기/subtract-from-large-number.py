num = input().split()
a, b = int(num[0]), int(num[1])
if a>b:
    print(a-b)
elif b>=a:
    print(b-a)