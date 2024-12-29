n = input().split()
a, b = int(n[0]), int(n[1])
res = False
for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        res = True
if res == True:
    print(1)
else:
    print(0)