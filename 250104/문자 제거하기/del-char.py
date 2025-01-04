s = input()

while len(s) > 1:
    index = int(input())

    if index >= len(s):
        s = s[:-1]
    else:
        s = s[:index] + s[index+1:]

    print(s)
