n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = False
k = 0
for i in range(n1):
    if k > n2-1:
        break
    if a[i] == b[k]:
        k += 1
        res = True
    else:
        res = False
        k = 0

if res:
    print("Yes")
else:
    print("No")