a, b = list(map(int, input().split()))
s = str(a + b)
cnt = 0
for e in s:
    if e == '1':
        cnt += 1
print(cnt)
