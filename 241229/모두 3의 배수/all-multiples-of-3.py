res = True
for _ in range(5):
    n = int(input())
    if n % 3 != 0:
        res = False

if res == True:
    print(1)
else:
    print(0)