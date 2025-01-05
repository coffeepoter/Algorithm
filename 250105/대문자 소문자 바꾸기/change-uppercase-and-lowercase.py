s = input()
for elem in s:
    if elem.islower():
        print(elem.upper(), end="")
    elif elem.isupper():
        print(elem.lower(), end="")