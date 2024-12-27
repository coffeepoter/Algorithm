num = input().split("-")
a, b = num[1], num[2]
a, b = b, a
print(f"{num[0]}-{a}-{b}")