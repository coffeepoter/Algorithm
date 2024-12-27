num = input().split()
a, b = int(num[0]), int(num[1])
max = a if a>=b else b
print(max)