s = input().split()
a, b = "", ""
for e in s[0]:
    if e.isdigit():
        a += e
    else:
        break
for e in s[1]:
    if e.isdigit():
        b += e
    else:
        break

print(int(a)+int(b))