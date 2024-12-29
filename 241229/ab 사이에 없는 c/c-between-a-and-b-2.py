n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])
res = False
for i in range(a,b+1):
    if i % c == 0:
        res = True
if res == True:
    print("NO")
else:
    print("YES")