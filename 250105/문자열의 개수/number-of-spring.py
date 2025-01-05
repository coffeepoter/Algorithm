arr = []
cnt = 0
while True:
    s = input()
    if s == '0':
        break
    cnt += 1
    if cnt % 2 == 1:
        arr.append(s)
print(cnt)
for e in arr:
    print(e)
    