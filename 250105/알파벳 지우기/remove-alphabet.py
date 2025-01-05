a = input()
b = input()
m, n = "", ""
for e in a:
    if e.isdigit():
        m += e
for e in b:
    if e.isdigit():
        n += e
print(int(m)+int(n))