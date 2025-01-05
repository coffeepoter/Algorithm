s = input().split('.')
for elem in s:
    if ord(elem[0]) < 67:
        continue
    print(elem.upper(), end="")