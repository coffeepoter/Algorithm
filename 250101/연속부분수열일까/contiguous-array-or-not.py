n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
y = x + n2
res = False

for _ in range(n1-n2+1):
    new_a = a[x:y]
    if new_a == b:
        res = True
        break
    else:
        x += 1
        y += 1

if res:
    print("Yes")
else:
    print("No")