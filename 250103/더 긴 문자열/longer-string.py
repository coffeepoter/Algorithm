words = input().split()
if len(words[0]) > len(words[1]):
    print(words[0], len(words[0]))
elif len(words[0]) < len(words[1]):
    print(words[1], len(words[1]))
else:
    print("same")